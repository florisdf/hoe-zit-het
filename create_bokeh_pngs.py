#!/usr/bin/env python
import json
from pathlib import Path
from bokeh.document import Document
import bokeh.io
from tqdm import tqdm
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force',
                    help='Create all pngs, even if their '
                    'source file didn\'t change.',
                    action='store_true')
args = parser.parse_args()
LAZY = ~args.force

docs = {p: Document.from_json(json.load(p.open())['doc'])
        for p in Path('content/lessen/').rglob('*/plt/*.json')}

for p, doc in tqdm(docs.items()):
    md5_file = p.parent / (p.stem + '.md5')
    m = hashlib.md5()
    m.update(p.read_bytes())
    cur_md5sum = m.digest()

    if not md5_file.exists():
        md5_file.write_bytes(cur_md5sum)

    prev_md5sum = md5_file.read_bytes()

    if prev_md5sum != cur_md5sum or not LAZY:
        md5_file.write_bytes(cur_md5sum)
        fn = p.parent / f'{p.stem}.png'
        fig = doc.roots[0]
        fig.sizing_mode = 'fixed'
        fig.toolbar_location = None
        fig.outline_line_alpha = 0
        bokeh.io.export_png(fig, fn, width=600, height=600)
