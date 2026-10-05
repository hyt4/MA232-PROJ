"""Export project.ipynb to report/MA232_Project1_Report.html (and .pdf via Chrome, if available).

Run after executing the notebook:  .venv/bin/python export_report.py

The notebook writes dollar signs as `\\$` (correct in Jupyter / VS Code). nbconvert's markdown
parser mishandles `\\$` and turns some of them into math, so the export works on a copy where
each `\\$` is replaced with HTML entities that MathJax still shows as a plain "$".
The notebook itself is never modified.
"""
import os
import subprocess

import nbformat
from nbconvert import HTMLExporter
from traitlets.config import Config

SRC = "project.ipynb"
OUT_DIR = "report"
NAME = "MA232_Project1_Report"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def protect_dollars(text):
    return text.replace("\\$", "&#92;&#36;")


nb = nbformat.read(SRC, as_version=4)
for cell in nb.cells:
    if cell.cell_type == "markdown":
        cell.source = protect_dollars(cell.source)
    for out in cell.get("outputs", []):
        if "text/markdown" in out.get("data", {}):
            out["data"]["text/markdown"] = protect_dollars(out["data"]["text/markdown"])

c = Config()
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_input_tags = ["hide-input"]
html, _ = HTMLExporter(config=c).from_notebook_node(nb)

os.makedirs(OUT_DIR, exist_ok=True)
html_path = os.path.abspath(os.path.join(OUT_DIR, NAME + ".html"))
with open(html_path, "w") as f:
    f.write(html)
print("Wrote", html_path)

if os.path.exists(CHROME):
    pdf_path = os.path.join(OUT_DIR, NAME + ".pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=20000", f"--print-to-pdf={pdf_path}", f"file://{html_path}"],
                   check=True, capture_output=True)
    print("Wrote", pdf_path)
else:
    print("Chrome not found; open the HTML in a browser and Print -> Save as PDF.")
