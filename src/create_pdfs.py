#!/usr/bin/env python
from pathlib import Path
from tqdm import tqdm
import logging
import subprocess

articles = list(Path('content/lessen').rglob('*/index.md'))

for p in tqdm(articles[:5]):
    bare_html = (Path(str(p).replace("content/",
                                    "public/bare/", 1)
                      .replace("index.md", "index.html")))
    lesson_html = Path(str(bare_html).replace("public/bare/", "public/", 1))

    logging.log(logging.WARNING, str(bare_html))
    logging.log(logging.WARNING, str(lesson_html))

    pdf_file = (lesson_html.parent
                / ('-'.join([lesson_html.parent.parent.name, 
                             lesson_html.parent.name]).title() + '.pdf'))
    args = ['wkhtmltopdf', '-T', '25mm', '-B', '25mm', '-R', '25mm', '-L',
            '25mm', '--no-stop-slow-scripts',
            '--javascript-delay', '5000', '--viewport-size', '1920x1080', '-',
            str(pdf_file)]
    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE)
    # Replace absolute refs by relative refs
    root_dir = Path('public').absolute()
    logging.log(logging.WARNING, str(root_dir))
    child_proccess.stdin.write(bare_html.read_text()
                               .replace('="/bare/', f'="{root_dir}/')
                               .encode('utf-8'))
    child_proccess.communicate()
    child_proccess.stdin.close()
   
    # Link to correct pdf-file by replacing href pattern in lesson html file
    pdf_link = str(pdf_file).replace('public/', '/', 1)
    new_html_content = (lesson_html.read_text()
                        .replace("##REPLACED_BY_CREATE_PDFS##", pdf_link))
    lesson_html.write_text(new_html_content)
