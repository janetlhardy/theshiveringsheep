#!/usr/bin/env python3
"""Rebuild every print file from the HTML sources.

    python3 build.py

Produces, from `business-cards.html`:
    business-card-front.pdf / .png     ← upload these to VistaPrint, one per side
    business-card-back.pdf  / .png
    business-cards.pdf                 ← both sides in one 2-page file, if ever wanted
    business-cards.png                 ← preview of both

and from `booth-banner.html`:
    booth-banner.pdf / .png / .jpg

The single-sided files exist because VistaPrint's business-card flow asks for
the front and the back separately. Handing it a 2-page PDF leaves you trying to
work out which page went where, which is exactly the confusion this avoids.

PNGs are written at 300 dpi. Some print sites place a PDF more predictably,
some an image — having both means never being stuck.

The HTML is the source of truth. Edit that, run this, never edit a PDF.
"""
import os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DPI = 300
CSS_DPI = 96          # what a CSS inch is worth before scaling

def chrome(*args):
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--virtual-time-budget=25000", *args],
                   cwd=HERE, capture_output=True)

def to_pdf(html, pdf):
    chrome("--no-pdf-header-footer", f"--print-to-pdf={pdf}",
           f"file://{os.path.join(HERE, html)}")
    print(f"  {pdf}")

def to_png(html, png, w_in, h_in, dpi=DPI):
    """Screenshot at `dpi` by asking Chrome for a matching device scale."""
    scale = dpi / CSS_DPI
    chrome(f"--force-device-scale-factor={scale}",
           f"--window-size={round(w_in*CSS_DPI)},{round(h_in*CSS_DPI)}",
           f"--screenshot={png}", f"file://{os.path.join(HERE, html)}")
    print(f"  {png}")

def one_side(which):
    """Write a temporary HTML holding just the front or just the back."""
    src = open(os.path.join(HERE, "business-cards.html")).read()
    other = "back" if which == "front" else "front"
    # drop the other card's <div class="card ..."> … </div> block
    pattern = r'<!-- ─+ page \d+: ' + other.upper() + r' ─+ -->.*?\n</div>\n'
    out = re.sub(pattern, "", src, flags=re.S)
    if 'class="card ' + other in out:
        sys.exit(f"could not strip the {other} card — has business-cards.html changed shape?")
    tmp = os.path.join(HERE, f"_tmp-{which}.html")
    open(tmp, "w").write(out)
    return f"_tmp-{which}.html", tmp

if __name__ == "__main__":
    if not os.path.exists(CHROME):
        sys.exit("Google Chrome not found — it does the PDF rendering.")

    print("business cards:")
    to_pdf("business-cards.html", "business-cards.pdf")
    to_png("business-cards.html", "business-cards.png", 3.75, 4.5, dpi=192)
    for which in ("front", "back"):
        rel, tmp = one_side(which)
        try:
            to_pdf(rel, f"business-card-{which}.pdf")
            to_png(rel, f"business-card-{which}.png", 3.75, 2.25)
        finally:
            os.remove(tmp)

    print("banner:")
    to_pdf("booth-banner.html", "booth-banner.pdf")
    to_png("booth-banner.html", "booth-banner.png", 72.5, 24.5, dpi=96)
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92",
                    "booth-banner.png", "--out", "booth-banner.jpg"],
                   cwd=HERE, capture_output=True)
    print("  booth-banner.jpg")
    print("done.")
