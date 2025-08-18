import requests
import gzip
import io
import time
import logging
import os
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree
from bs4 import BeautifulSoup
import PyPDF2

# Configuration
CACERT_PATH = "F:/pdf_auditor/src/pdf_auditor/utils/certs/cacert.pem"
USER_AGENT = "PDFAuditorBot/1.0"
RATE_LIMIT = 1  # seconds between requests
MAX_CRAWL_DEPTH = 2

# Initialize logger
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO
)
logger = logging.getLogger("pdf_auditor")


def scrape_pdfs(start_url: str, output_dir: str) -> None:
    """
    Main entry point: discovers PDFs via sitemap or crawl and downloads them.
    """
    # Prepare
    parsed = urlparse(start_url)
    domain = parsed.netloc
    base_output = Path(output_dir) / domain
    base_output.mkdir(parents=True, exist_ok=True)

    # 1. Fetch robots.txt rules
    robots_txt = fetch_robots_txt(domain)
    sitemap_urls, disallows = parse_robots_txt(robots_txt)

    # 2. Fallback sitemap if none
    if not sitemap_urls:
        sitemap_urls = [f"https://{domain}/sitemap.xml"]

    # 3. Expand nested sitemapindexes
    final_sitemaps = []
    for sm_url in sitemap_urls:
        try:
            raw = fetch(sm_url)
            xml = maybe_decompress(raw)
            if b'<sitemapindex' in xml:
                final_sitemaps += parse_sitemapindex(xml)
            else:
                final_sitemaps.append(sm_url)
        except Exception as e:
            logger.warning(f"Failed to fetch/parse sitemap {sm_url}: {e}")

    # 4. Collect URLs
    all_urls = set()
    for sm in final_sitemaps:
        try:
            raw = fetch(sm)
            xml = maybe_decompress(raw)
            locs = parse_sitemap_xml(xml)
            all_urls.update(locs)
        except Exception as e:
            logger.warning(f"Error parsing sitemap {sm}: {e}")

    # 5. Filter by domain and disallows
    pdf_urls, html_urls = [], []
    for url in all_urls:
        p = urlparse(url)
        if p.netloc != domain:
            continue
        if any(p.path.startswith(d) for d in disallows):
            logger.info(f"Skipping disallowed path: {url}")
            continue
        if p.path.lower().endswith('.pdf'):
            pdf_urls.append(url)
        else:
            html_urls.append(url)

    # Manifest for tracking
    manifest = {}

    # 6. Download PDFs from sitemap
    for url in pdf_urls:
        record = download_and_save_pdf(url, base_output)
        manifest[url] = record
        time.sleep(RATE_LIMIT)

    # 7. Crawl HTML pages for embedded PDFs
    for page_url in html_urls:
        try:
            html = fetch(page_url).decode('utf-8', errors='ignore')
            links = parse_html_links(html)
            for href in links:
                if '.pdf' in href.lower():
                    pdf_link = urljoin(page_url, href)
                    p = urlparse(pdf_link)
                    if p.netloc != domain or any(p.path.startswith(d) for d in disallows):
                        continue
                    record = download_and_save_pdf(pdf_link, base_output)
                    manifest[pdf_link] = record
                    time.sleep(RATE_LIMIT)
        except Exception as e:
            logger.warning(f"Failed to crawl HTML {page_url}: {e}")

    # 8. Optional fallback crawl
    if not final_sitemaps or (len(pdf_urls) + len(html_urls) == 0):
        logger.info("No sitemaps or URLs found; falling back to crawl")
        crawl_for_pdfs(start_url, base_output, disallows, manifest)

    # 9. Write manifest
    manifest_path = base_output / 'manifest.json'
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    logger.info(f"Manifest written to {manifest_path}")


# Helper functions

def fetch(url: str) -> bytes:
    headers = {'User-Agent': USER_AGENT}
    resp = requests.get(url, headers=headers, timeout=10, verify=CACERT_PATH)
    resp.raise_for_status()
    return resp.content


def fetch_robots_txt(domain: str) -> str:
    try:
        content = fetch(f"https://{domain}/robots.txt").decode('utf-8', errors='ignore')
        return content
    except Exception:
        return ''


def parse_robots_txt(text: str):
    sitemaps, disallows = [], []
    for line in text.splitlines():
        if line.lower().startswith('sitemap:'):
            sitemaps.append(line.split(':',1)[1].strip())
        elif line.lower().startswith('disallow:'):
            path = line.split(':',1)[1].strip()
            if path:
                disallows.append(path)
    return sitemaps, disallows


def maybe_decompress(raw: bytes) -> bytes:
    # Detect and decompress .gz
    if raw[:2] == b'\x1f\x8b':
        buf = io.BytesIO(raw)
        with gzip.GzipFile(fileobj=buf) as gz:
            return gz.read()
    return raw


def parse_sitemap_xml(xml: bytes) -> list:
    tree = ElementTree.fromstring(xml)
    return [elem.text for elem in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]


def parse_sitemapindex(xml: bytes) -> list:
    tree = ElementTree.fromstring(xml)
    return [elem.text for elem in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]


def parse_html_links(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    return [a.get('href') for a in soup.find_all('a', href=True)]


def download_and_save_pdf(url: str, output_dir: Path) -> dict:
    record = {'path': None, 'status': None, 'error': None}
    try:
        # HEAD check
        h = requests.head(url, headers={'User-Agent': USER_AGENT}, timeout=10, verify=CACERT_PATH)
        if 'application/pdf' not in h.headers.get('Content-Type', ''):
            record['status'] = 'skipped_non_pdf'
            logger.info(f"Skipping non-PDF: {url}")
            return record

        # Prepare local path
        parsed = urlparse(url)
        local_path = output_dir / parsed.path.lstrip('/')
        local_path.parent.mkdir(parents=True, exist_ok=True)

        # Download
        with requests.get(url, headers={'User-Agent': USER_AGENT}, stream=True, timeout=20, verify=CACERT_PATH) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        record['path'] = str(local_path)
        record['status'] = 'downloaded'

        # Validate
        if not validate_pdf_file(local_path):
            record['status'] = 'invalid_pdf'
            logger.warning(f"Invalid PDF file: {local_path}")
        else:
            logger.info(f"Downloaded: {url} -> {local_path}")
    except Exception as e:
        record['error'] = str(e)
        logger.error(f"Error downloading {url}: {e}")
    return record


def validate_pdf_file(path: Path) -> bool:
    try:
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            # Try reading number of pages
            _ = len(reader.pages)
        return True
    except Exception:
        return False


def crawl_for_pdfs(start_url: str, output_dir: Path, disallows: list, manifest: dict):
    queue = [(start_url, 0)]
    visited = set()
    while queue:
        url, depth = queue.pop(0)
        if depth > MAX_CRAWL_DEPTH or url in visited:
            continue
        visited.add(url)
        try:
            html = fetch(url).decode('utf-8', errors='ignore')
            links = parse_html_links(html)
            for href in links:
                abs_url = urljoin(url, href)
                p = urlparse(abs_url)
                if p.netloc != urlparse(start_url).netloc:
                    continue
                if any(p.path.startswith(d) for d in disallows):
                    continue
                if p.path.lower().endswith('.pdf'):
                    record = download_and_save_pdf(abs_url, output_dir)
                    manifest[abs_url] = record
                    time.sleep(RATE_LIMIT)
                else:
                    queue.append((abs_url, depth + 1))
        except Exception as e:
            logger.warning(f"Crawl error at {url}: {e}")


# Example usage:
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="PDF Auditor: sitemap-driven PDF scraper")
    parser.add_argument('start_url', help='Starting URL of the website to scrape')
    parser.add_argument('output_dir', help='Directory to save downloaded PDFs')
    args = parser.parse_args()
    scrape_pdfs(args.start_url, args.output_dir)
