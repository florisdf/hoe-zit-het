#!/usr/bin/env python
import subprocess

subprocess.run('hugo && firebase deploy', shell=True)
subprocess.run('./create_bokeh_pngs.py')
subprocess.run('./create_pdfs.py')
subprocess.run('hugo && firebase deploy', shell=True)
