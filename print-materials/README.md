# The Shivering Sheep — Print Materials

Designed to match the website: the **Caveat** wordmark in its pink → purple → turquoise gradient,
**Boogaloo** for the tagline, **Nunito** for the details, on the site's near-black `#0D0020`.

_This folder is kept off the public website._

## What's in here

| File | What it is | Finished size | Order it as… |
|---|---|---|---|
| `business-card-front.pdf` | **Upload this to the front** | 3.5 × 2 in | Standard business cards, **double-sided** |
| `business-card-back.pdf` | **Upload this to the back** | 3.5 × 2 in | (same order) |
| `business-cards.pdf` | Both sides in one 2-page file, if a printer wants that instead | 3.5 × 2 in | — |
| `business-card-front.png`, `business-card-back.png` | The same two sides as 300 dpi images, if a site handles a PDF badly | 3.5 × 2 in | — |
| `booth-banner.pdf` | **The file you upload** | 72 × 24 in trimmed (file is 72.5 × 24.5 with bleed) | Vinyl banner, **6 ft × 2 ft**, hemmed with grommets |
| `booth-banner.jpg` | The same banner as an image, if a site won't take the PDF | 72 × 24 in | — |

The `.html` files are the editable source. **Edit those, then run `python3 build.py`** — it
regenerates every PDF and PNG in one go. Never edit a PDF directly; the next build would overwrite
it. `cutouts.py` is explained at the bottom.

## What's on them

**The card.** Front: the name, `HAND-KNIT · FELTED · ONE OF A KIND`, the website and the email
address. Back: one bag on cream, with the name and website again. **No Instagram** — you don't post
there, and a handle that leads to an empty feed does more harm than no handle at all.

**The banner.** The name large enough to read across a hall, the tagline, the website, and four bags
straight on the dark ground: *Circle Back*, the **Purple / Hot Pink striped tote**, *Shadow Play*
and *Bullseye*.

Three deliberate choices in that line-up:

- **One is a striped tote**, because the striped totes are most of the stock and the banner should
  show what's actually on the table.
- **Nothing seasonal.** The snowflake tote *Nordic Flurry* was here first and came back out — this
  banner has to work at a summer market as well as a Christmas one.
- **Shadow Play carries the warm colours.** The other three are blue-dominant, so it's the one
  bringing orange, yellow and green. Mondrian was the alternative but would have added a third blue.

There's no cream panel behind them any more. An earlier version had one, because the photographs
came on a white studio background and each bag sat in a visible pale rectangle. Once `cutouts.py`
made them properly transparent the panel was only adding dead space, so the bags went straight onto
the dark with a soft pool of light behind them. **No QR code**, deliberately: hung behind a table it sits too far away for a phone
to focus on, so it would be decoration pretending to be useful.

## Ordering from VistaPrint

**Business cards**

1. Business Cards → Standard → **3.5 × 2 in**, and choose **double-sided** (printed both sides).
2. Pick the option like **"Upload your complete design"** — not one of their templates.
3. There are **two separate slots, Front and Back**. Put `business-card-front.pdf` in the front one
   and `business-card-back.pdf` in the back one. That's why they're separate files: hand VistaPrint
   the 2-page `business-cards.pdf` and you're left guessing which page went where.
4. If it asks about bleed, the files already have it: say **yes / keep bleed**.

**If the artwork lands small in the top-left corner** — that's their uploader placing the file
without scaling it, exactly as it does with the banner. **Press `Fill`**, or drag the corner handle
out until the design covers the whole card. It will crop a sliver as it scales, which is what the
bleed is for. Nothing is wrong with the file.

**If the PDF misbehaves**, upload `business-card-front.png` and `business-card-back.png` instead.
Same artwork, 300 dpi, and some sites place an image more predictably than a PDF.

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

Source JPEGs for the alternatives Janet shortlisted are already in `images/`, so swapping one in is
a single command: **Forest Green / Hot Pink**, **Hot Pink / Neon Blue**, **Mondrian**, **Hypnotic**,
**Spiral Rose** and **Nordic Flurry** (the snowflake tote, if a Christmas-only version is ever
wanted). Note `cutouts.py` regenerates a PNG for *every* `bag-*.jpeg` it finds, so delete the ones
you aren't using afterwards — they're 3 MB each and the folder grows quickly.

## Want changes?

Tell Claude — different bags, different wording, a table sign as well, price cards for the show.
Everything rebuilds from the HTML with `python3 build.py`, which drives headless Chrome.
