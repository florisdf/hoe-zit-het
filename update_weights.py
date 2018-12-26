#!/usr/bin/env python
from pathlib import Path
import re

p = Path('./content/lessen/')

# Remove lines from order.txt that are obsolete
for order in p.glob('*/*/order.txt'):
    good_lines = [l for l in order.open().readlines()
                  if (order.parent / l[:-1] / 'index.md').exists()]
    order.open('w').writelines(good_lines)

# Add files to order.txt
for idx in p.glob('*/*/*/index.md'):
    order = idx.parent.parent / 'order.txt'

    # Create empty order.txt if it does not exist
    if not order.exists():
        order.write_text('\n')

    if not any([re.search(f'^{idx.parent.stem}\n', l)
                for l in order.open().readlines()]):
        order.open('a').write(f'{idx.parent.stem}\n')

# Change the weights to their line number in the order.txt file
for order in p.glob('*/*/order.txt'):
    for i, il in enumerate(order.open().readlines()):
        idx = (order.parent / il[:-1] / 'index.md')
        idx_lines = idx.open().readlines()
        for j, jl in enumerate(idx_lines):
            if re.search('^weight: ', jl):
                break
        idx_lines[j] = f'weight: {i + 1}\n'
        idx.open('w').writelines(idx_lines)
