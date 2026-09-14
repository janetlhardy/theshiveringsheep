#!/usr/bin/env python3
"""Turn the bag photos into transparent PNGs for the print designs.

The product shots sit on a white studio background. Dropped onto a coloured
panel they each show up inside a pale rectangle, so the background has to go.

Two passes:

1. Flood-fill inward from the border, which copes with the soft shadow that
   fades from the bag out into the background.
2. Clear anything left that matches the studio background exactly. Every one
   of these photos was shot on the same flat neutral grey-white — measured at
   (246, 246, 246) with *zero* difference between the channels — whereas the
   cream wool in the design is warmer and textured (about 233, with a spread
   of 13 across the channels). So "perfectly neutral and very pale" picks out
   the backdrop and leaves Bullseye's white rings and Nordic Flurry's cream
   snowflakes untouched. This second pass is what clears background trapped
   inside a strap loop, which no fill from the border can reach.

    python3 cutouts.py          # images/*.jpeg -> images/cut-*.png
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
KEY  = (255, 0, 255)   # a colour no wool photo contains
THRESH = 46            # how far from the seed colour still counts as background
STEP = 6               # seed every Nth pixel along the border
FLAT_MIN = 240         # pass 2: how pale a pixel must be to count as backdrop
FLAT_SPREAD = 5        # pass 2: and how neutral (max channel - min channel)

def cut(src, dst):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    d = ImageDraw.floodfill  # fills only the connected region it starts in
    # Seed all the way along every edge, not just the corners. A strap or a
    # soft shadow can pinch the background into several separate regions that
    # each touch the border somewhere unpredictable.
    seeds  = [(x, 0) for x in range(0, w, STEP)]
    seeds += [(x, h-1) for x in range(0, w, STEP)]
    seeds += [(0, y) for y in range(0, h, STEP)]
    seeds += [(w-1, y) for y in range(0, h, STEP)]
    for s in seeds:
        px = im.getpixel(s)
        if px == KEY:                         # already cleared by an earlier fill
            continue
        if sum(px)/3 > 200:                   # only seed on a pale pixel
            d(im, s, KEY, thresh=THRESH)
    im = im.convert("RGBA")
    px = im.load()
    n = 0
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            if (r, g, b) == KEY:
                px[x, y] = (255, 255, 255, 0); n += 1
            elif min(r, g, b) >= FLAT_MIN and max(r, g, b) - min(r, g, b) <= FLAT_SPREAD:
                px[x, y] = (255, 255, 255, 0); n += 1   # backdrop inside a strap loop
    im.save(dst)
    return n / (w*h)

if __name__ == "__main__":
    for f in sorted(os.listdir(HERE)):
        if not f.endswith(".jpeg") or f.startswith("cut-"):
            continue
        out = os.path.join(HERE, "cut-" + f.replace(".jpeg", ".png"))
        share = cut(os.path.join(HERE, f), out)
        print("%-26s background removed: %4.1f%%" % (f, share*100))
