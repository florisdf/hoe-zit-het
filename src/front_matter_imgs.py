import re
from pathlib import Path

lessons = [*Path('content/lessen/').rglob('*.md')]

for lesson in lessons:
    matches = re.finditer('{{% (img|svg|bokeh) "([^"]*)" %}}', lesson.read_text())
    imgs = [m.group(2).replace('.svg', '.png').replace('.json', '.png')
            for m in matches]
    imgs = ['/' + ''.join(str(lesson.parent).split('content/')[1:]) + '/' + img
            for img in imgs]

    lines = lesson.read_text().split('\n')
    idxs = [i for i, l in enumerate(lines) if re.match('images: \[.*\]', l)]
    if len(idxs) == 1:
        idx = idxs[0]
        lines[idx] = f"images: {imgs}"
    else:
        idx = [i for i, l in enumerate(lines) if l == '---'][1]
        lines.insert(idx, f"images: {imgs}")

    lesson.write_text('\n'.join(lines))
