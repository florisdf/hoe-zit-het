#!/usr/bin/env python
import subprocess
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force',
                    help='Create all pdfs and pngs, even if their '
                    'source file didn\'t change.',
                    action='store_true')
args = parser.parse_args()
LAZY = not args.force


curdir = Path(__file__).parent
subprocess.run('hugo && firebase deploy', shell=True)
if LAZY:
    subprocess.run(str(curdir / 'create_bokeh_pngs.py'))
    subprocess.run(str(curdir / 'create_pdfs.py'))
else:
    subprocess.run(str(curdir / 'create_bokeh_pngs.py -f'), shell=True)
    subprocess.run(str(curdir / 'create_pdfs.py -f'), shell=True)
subprocess.run('hugo && firebase deploy', shell=True)
