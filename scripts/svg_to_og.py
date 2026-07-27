#!/usr/bin/env python3
"""Rasterize an SVG diagram to a 1200x630 OG image, center-cropped to the exact aspect ratio.

Usage: python3 svg_to_og.py input.svg output.png

Requires cairosvg + pillow. In WSL, with no system-wide install:
    python3 -m venv --without-pip ~/ogimg-venv/venv
    curl -s https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
    ~/ogimg-venv/venv/bin/python3 /tmp/get-pip.py --quiet
    ~/ogimg-venv/venv/bin/pip install --quiet cairosvg pillow
    ~/ogimg-venv/venv/bin/python3 scripts/svg_to_og.py input.svg output.png
"""
import sys

import cairosvg
from PIL import Image

TARGET_W, TARGET_H = 1200, 630
# Render oversized so cropping to the exact target never leaves a hard edge.
RENDER_W, RENDER_H = 1250, 677


def main(svg_path: str, out_path: str) -> None:
    raw = "/tmp/_svg_to_og_raw.png"
    cairosvg.svg2png(
        url=svg_path, write_to=raw,
        output_width=RENDER_W, output_height=RENDER_H,
        background_color="white",
    )
    img = Image.open(raw).convert("RGB")
    w, h = img.size
    left = (w - TARGET_W) // 2
    top = (h - TARGET_H) // 2
    img.crop((left, top, left + TARGET_W, top + TARGET_H)).save(out_path, "PNG")
    print(f"saved {out_path} ({TARGET_W}x{TARGET_H})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(f"usage: {sys.argv[0]} input.svg output.png")
    main(sys.argv[1], sys.argv[2])
