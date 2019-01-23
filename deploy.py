#!/usr/bin/env python
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force',
                    help='Create all pdfs and pngs, even if their '
                    'source file didn\'t change.',
                    action='store_true')
args = parser.parse_args()
LAZY = ~args.force


subprocess.run('hugo && firebase deploy', shell=True)
if LAZY:
    subprocess.run('./create_bokeh_pngs.py')
    subprocess.run('./create_pdfs.py')
else:
    subprocess.run('./create_bokeh_pngs.py -f', shell=True)
    subprocess.run('./create_pdfs.py -f', shell=True)
subprocess.run('hugo && firebase deploy', shell=True)
