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
                                              1)).absolute()

    logging.log(logging.WARNING, str(bare_html))
    logging.log(logging.WARNING, 'Contents:')
    logging.log(logging.WARNING, '\n'.join(list(bare_html.parent.iterdir())))

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
    html_content = bare_html.read_text()
    
    for match in re.finditer(r'="/bare/[^"]*"', html_content):
        src_path = match.group(0)
        new_src_path = src_path.replace('="/bare/', f'="{root_dir}/')
        logging.log(logging.WARNING, new_src_path)
        logging.log(logging.WARNING, f'Exists? {Path(new_src_path).exists()}')
                
    # child_proccess.stdin.write(html _content
    #                            .replace('="/bare/', f'="{root_dir}/')
    #                            .encode('utf-8'))
    # child_proccess.communicate()
    # child_proccess.stdin.close()
   
    # Link to correct pdf-file by replacing href pattern in lesson html file
    pdf_link = str(pdf_file).replace('public/', '/', 1)
    new_html_content = (lesson_html.read_text()
                        .replace("##REPLACED_BY_CREATE_PDFS##", pdf_link))
    lesson_html.write_text(new_html_content)
