#!/usr/bin/env python
from pathlib import Path
from tqdm import tqdm
import logging
import subprocess

articles = list(Path('content/lessen').rglob('*/index.md'))

for p in tqdm(articles):
    url = Path(str(p).replace("content/", "public/", 1).replace("index.md", "index.html"))
    pdf_file = url.parent / ('-'.join([url.parent.name, url.parent.parent.name]).title() + '.pdf')
    args = ['wkhtmltopdf', '-', '-T', '25mm', '-B', '25mm', '-R', '25mm', '-L',
            '25mm', '--no-stop-slow-scripts',
            '--javascript-delay', '5000', '--viewport-size', '1920x1080',
            str(pdf_file)]
    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE)
    child_proccess.stdin.write(url.read_text())
    child_proccess.communicate()
    child_proccess.stdin.close()