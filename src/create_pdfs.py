#!/usr/bin/env python
from pathlib import Path
from tqdm import tqdm
import logging
import subprocess
import re

articles = list(Path('content/lessen').rglob('*/index.md'))

for p in tqdm(articles[4:5]):
    bare_html = (Path(str(p).replace("content/",
                                    "public/bare/", 1)
                      .replace("index.md", "index.html")).absolute())
    lesson_html = Path(str(bare_html).replace("public/bare/", "public/",
                                              1))

    pdf_file = (lesson_html.parent
                / ('-'.join([lesson_html.parent.parent.name, 
                             lesson_html.parent.name]).title() + '.pdf'))
    args = ['xvfb-run', '-a', '--server-args', '-screen 0, 1920x1080x24',
            'wkhtmltopdf', '-T', '25mm', '-B', '25mm', '-R', '25mm', '-L',
            '25mm', '--no-stop-slow-scripts', '--enable-local-file-access', 
            '--enable-internal-links', '--javascript-delay', '5000', '--viewport-size',
            '1920x1080',
            '-', str(pdf_file)]
    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
    # Replace absolute refs by relative refs
    root_dir = Path('public').absolute()
    html_content = bare_html.read_text()

    for match in re.finditer(r'href="(\.\./[^"]*)"', html_content):
        href_path = str((lesson_html.parent / match.group(1)).resolve())
        slug_match = re.search('^.*/public/(.*)$', href_path)
        if slug_match:
            new_href = f'href="https://hoezithet.nu/{slug_match.group(1)}"'
            html_content = html_content.replace(match.group(0), new_href)

    child_proccess.stdin.write(html_content.encode('utf-8'))
    outs, errs = child_proccess.communicate()
    while 'RemoteHostClosedError' in str(outs):
        outs, errs = child_proccess.communicate()
    child_proccess.stdin.close()
   
    # Link to correct pdf-file by replacing href pattern in lesson html file
    pdf_link = str(pdf_file).replace('public/', '/', 1)
    new_html_content = (lesson_html.read_text()
                        .replace("##REPLACED_BY_CREATE_PDFS##", pdf_link))
    lesson_html.write_text(new_html_content)
