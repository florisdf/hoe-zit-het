#!/usr/bin/env python
"""
Updates the weights of each "les" in "content/lessen". This way we can order
the tutorials in any way we want by updating the "order.txt" file that is
present in each "lessen" section.
"""
from pathlib import Path
import re

p = Path('./content/lessen/')

# Remove lines from order.txt that are obsolete
for order in p.rglob('*/order.txt'):
    good_lines = [l for l in order.open().readlines()
                  if ((order.parent / l[:-1] / 'index.md').exists()
                      or (order.parent / l[:-1] / '_index.md').exists())]
    order.open('w').writelines(good_lines)

# Add files to order.txt
for idx in p.rglob('*/*index.md'):
    order = idx.parent.parent / 'order.txt'

    # Create empty order.txt if it does not exist
    if not order.exists():
        order.write_text('\n')

    if not any([re.search(f'^{idx.parent.stem}\n', l)
                for l in order.open().readlines()]):
        order.open('a').write(f'{idx.parent.stem}\n')

# Change the weights to their line number in the order.txt file
for order in p.rglob('*/*order.txt'):
    for i, il in enumerate(order.open().readlines()):
        idx = (order.parent / il[:-1] / 'index.md')
        if not idx.exists():
            idx = (order.parent / il[:-1] / '_index.md')
        assert idx.exists()

        idx_lines = idx.open().readlines()
        in_frontmatter = False
        for j, jl in enumerate(idx_lines):
            if re.search('^---', jl):
                in_frontmatter = ~in_frontmatter
            if not in_frontmatter:
                break
            if re.search('^weight: ', jl):
                break

        if in_frontmatter:
            idx_lines[j] = f'weight: {i + 1}\n'
        else:
            # "weight" was not yet a key in the front matter
            idx_lines.insert(j, f'weight: {i + 1}\n')
        idx.open('w').writelines(idx_lines)
