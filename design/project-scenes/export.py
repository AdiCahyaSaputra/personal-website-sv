# /// script
# dependencies = ["pillow"]
# ///
"""Export Blender renders as optimized website images: uv run design/project-scenes/export.py."""
from pathlib import Path

from PIL import Image

directory = Path(__file__).resolve().parents[2] / 'static/assets/project-scenes'

for source in sorted(directory.glob('*-macbook.png')):
    target = source.with_name(source.stem.removesuffix('-macbook') + '.webp')

    with Image.open(source) as image:
        image.convert('RGB').save(target, quality=95, method=6)

    print(f'{target.name}: {target.stat().st_size / 1024:.0f} KB')
