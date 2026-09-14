# The Shivering Sheep — Print Materials

Designed to match the website: the **Caveat** wordmark in its pink → purple → turquoise gradient,
**Boogaloo** for the tagline, **Nunito** for the details, on the site's near-black `#0D0020`.

_This folder is kept off the public website._

## What's in here

| File | What it is | Finished size | Order it as… |
|---|---|---|---|
| `business-cards.pdf` | 2 pages: front + back | 3.5 × 2 in | Standard business cards, **double-sided** |
| `booth-banner.pdf` | **The file you upload** | 72 × 24 in trimmed (file is 72.5 × 24.5 with bleed) | Vinyl banner, **6 ft × 2 ft**, hemmed with grommets |
| `booth-banner.jpg` | The same banner as an image, if a site won't take the PDF | 72 × 24 in | — |

The `.html` files are the editable source, the `.png` files are previews to look at, and
`cutouts.py` is explained at the bottom.

## What's on them

**The card.** Front: the name, `HAND-KNIT · FELTED · ONE OF A KIND`, the website and the email
address. Back: one bag on cream, with the name and website again. **No Instagram** — you don't post
there, and a handle that leads to an empty feed does more harm than no handle at all.

**The banner.** The name large enough to read across a hall, the tagline, the website, and four bags
on a cream panel. **No QR code**, deliberately: hung behind a table it sits too far away for a phone
to focus on, so it would be decoration pretending to be useful.

## Ordering from VistaPrint

**Business cards** — Business Cards → Standard → **3.5 × 2 in**, **double-sided**, upload
`business-cards.pdf`. If it asks about bleed, the file already has it: say **yes / keep bleed**.

**Banner** — Signs & Banners → Vinyl Banners → set the size to **6 ft × 2 ft (72 × 24 in)**. It has
to match, or they will scale the artwork. Choose the option like **"Upload your complete design"**
rather than one of their templates, then upload `booth-banner.pdf`. Ask for **hemmed edges with
grommets** so it can be tied up.

### If it says "extend your design to the edges"

**Press `Fill` in their editor.** Their uploader drops the file onto their canvas without scaling
it, so white shows *around* the artwork — the gap is in their layout, not in the file. `Fill` scales
it until it covers and the warning goes. It crops slightly as it scales, which is exactly what the
bleed is for: it eats the sacrificial quarter-inch and leaves the design untouched.

### If it warns about resolution

Safe to ignore on the banner. Their checker is calibrated for business cards. A 6 ft banner is read
from several feet away, and the lettering is vector so it prints at whatever resolution is asked
for. What's worth checking on their proof is the **framing** — name centred and unclipped, website
line complete, bags not stretched.

### About bleed — why the banner file is 72.5 × 24.5

That extra quarter-inch on every side is **bleed**: the design deliberately runs past where the
banner gets cut, so a slightly off cut can't leave a white sliver down one edge. The finished banner
is still 6 ft × 2 ft. Never export at exact trim size — `Fill` would then crop into the lettering.

## The bags — `cutouts.py`

The product photos were shot on a white studio background. Dropped onto the cream panel each one
showed up inside a visible pale rectangle, so the background had to be removed. `cutouts.py` makes
transparent PNGs (`images/cut-*.png`) and runs in two passes:

1. **Flood-fill inward from the border**, which copes with the soft shadow fading from the bag out
   into the backdrop.
2. **Clear anything left that matches the backdrop exactly.** Every photo was shot on the same flat
   neutral grey-white — measured at `(246, 246, 246)` with *zero* difference between the channels —
   while the cream wool in the designs is warmer and textured (about 233, with a spread of 13). So
   "perfectly neutral and very pale" picks out the backdrop and leaves **Bullseye's white rings** and
   **Nordic Flurry's cream snowflakes** alone. This pass is what clears background trapped inside a
   strap loop, which no fill from the border can reach.

To use different bags: copy them into `images/` as `bag-<name>.jpeg`, run `python3 cutouts.py`, and
point the HTML at the new `cut-bag-<name>.png`. **Check the result on a dark background** — that's
where a missed patch shows up.

## Want changes?

Tell Claude — different bags, different wording, a table sign as well, price cards for the show.
The PDFs are regenerated from the HTML with headless Chrome.
