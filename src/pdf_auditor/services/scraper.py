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
USER_AGENT = "PDFAuditorBot/1.0"
RATE_LIMIT = 1 # seconds between requests
MAX_CRAWL_DEPTH = 2

# Initialize logger
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO
)
logger = logging.getLogger("pdf_auditor")

def scrape_pdfs(start_url: str, output_dir: str) -> None:
    '''
    Main entry point: discovers PDFs via sitemap or crawl and downloads them
    '''
    # Prepare
    parsed = urlparse(start_url)
    domain = parsed.netloc
    base_output = Path(output_dir) / domain
    base_output.mkdir(parents=True, exist_ok=True)

    # 1. Fetch robots.txt rules
    robots_txt = fetch_robots_txt(domain)
    sitemap_urls, disallows = parse_robots_txt(robots_txt)

# Helper functions

def fetch(url: str) -> bytes:
    headers = {'User-Agent': USER_AGENT}
    resp = requests.get(url, headers=headers, timeout=10)
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
            sitemaps.append(line.split(":",1)[1].strip())
        elif line.lower().startswith('disallow:'):
            path = line.split(':',1)[1].strip()
            if path:
                disallows.append(path)
    return sitemaps, disallows