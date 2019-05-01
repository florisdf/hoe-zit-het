from pathlib import Path
import subprocess
from tqdm import tqdm

DPI = 150

for svg in tqdm(Path('./content').absolute().rglob('*.svg')):
    subprocess.run(['inkscape',
                    '-f', str(svg),
                    '-e', f'{svg.parent / svg.stem}.png',
                    '-d', str(DPI),
                    '-y', '0'])
