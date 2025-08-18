from pathlib import Path
p = Path(r"F:/pdf_auditor/src/pdf_auditor/utils/certs/cacert.pem")  # use your exact path, raw string
print("exists:", p.exists(), "size:", p.stat().st_size if p.exists() else 0)
print("first bytes:", open(p, "rb").read(32))
