#!/usr/bin/env python
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError
from tqdm import tqdm
import logging
from subprocess import run
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force',
                    help='Create all pdfs, even if their '
                    'source file didn\'t change.',
                    action='store_true')
args = parser.parse_args()
LAZY = not args.force

articles = list(Path('content/lessen').rglob('*/index.md'))

logging.info('Checking urls...')
for p in tqdm(articles):
    url = f'file://{Path(str(p).replace("content/", "public/", 1).replace("index.md", "index.html")).absolute}'
    md5_file = p.parent / (p.stem + '.md5')
    m = hashlib.md5()
    m.update(p.read_bytes())
    cur_md5sum = m.digest()

    if not md5_file.exists():
        md5_file.write_bytes(cur_md5sum)
        prev_md5sum = None
    else:
        prev_md5sum = md5_file.read_bytes()

    if prev_md5sum != cur_md5sum or not LAZY:
        md5_file.write_bytes(cur_md5sum)
        try:
            url_elements = url.split('/')[1:]
            print(*url_elements)
            pdf_dir = Path('content/lessen/' + '/'.join(url_elements))
            pdf_file = pdf_dir / ('-'.join(url_elements[-2:]).title() + '.pdf')
            run(['wkhtmltopdf', '-T', '25mm', '-B', '25mm', '-R', '25mm', '-L',
                 '25mm', url, '--no-stop-slow-scripts',
                '--javascript-delay', '5000', '--viewport-size', '1920x1080',
                 str(pdf_file)])
        except HTTPError as e:
            logging.info(f'{url} returned {e.code}')
