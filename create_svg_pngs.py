#!/usr/bin/env python
from pathlib import Path
import subprocess
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dpi',
                    help='output DPI (dots per inch)',
                    default=150, type=int)
parser.add_argument('-i', '--ignore',
                    help='ignore this file',
                    action='append')
parser.add_argument('path',
                    help='path to SVG file or directory with SVG files '
                    '(default "./content")',
                    default='./content')
args = parser.parse_args()
ignore = ([Path(p).absolute() for p in args.ignore]
          if args.ignore is not None else [])
path = Path(args.path).absolute()
svgs = [p for p in path.rglob('*.svg')
        if p not in ignore] if path.is_dir() else [path]

for svg in tqdm(svgs):
    subprocess.run(['inkscape',
                    '-f', str(svg),
                    '-e', f'{svg.parent / svg.stem}.png',
                    '-d', str(args.dpi),
                    '-y', '0'])
