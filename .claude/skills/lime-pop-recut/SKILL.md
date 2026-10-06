---
name: lime-pop-recut
description: House style learned from a reference 9:16 talking-head ad (a 16.9s agency hook): "Lime Pop". Use whenever the user asks for "that style", "like the reference/paidpro video", "lime captions", a punchy talking-head ad / hook / reel with stacked kinetic captions, or names any of its parts (lime hero word, strikethrough word, REC viewfinder, red alert cards, ring pip, stripe-flash transition, blur-through cut). Gives exact fonts, palette, sizes, placement, motion timings, transitions, SFX map, and a working HyperFrames template. Load /hyperframes-core first for the composition contract.
---

# Lime Pop — talking-head ad style

Learned frame by frame from a 720×1280, 30 fps, 16.9 s reference ad (founder talking to camera,
dark office set, one B-roll insert). Timestamps, measurements and colors below were measured from
the file (frame sampling, pixel sampling, luma and band-energy analysis, spectrograms), not guessed.
Full beat-by-beat breakdown: [references/reference-breakdown.md](references/reference-breakdown.md).
Working composition: [templates/lime-pop.html](templates/lime-pop.html) (passes `hyperframes check`:
0 lint / 0 layout issues, 21/21 contrast, tested on `assets/source.mp4`). Fonts: Inter and Sora, SIL OFL 1.1.

All pixel values below are for a **1080×1920** canvas (reference ×1.5).

## 1. The idea in one line

Dark, moody, voice-only footage. Every phrase becomes a **3-tier stacked caption**: one giant
**acid-lime hero word** framed by small **white lead-in / tail words** pinned to its edges. Each
beat swaps in a different **UI prop** (strikethrough, arrow cursor, REC viewfinder, error toasts,
chat pill, focus ring). Cuts are **jump cuts on silences**, hidden by **blur-through** or a
**stripe flash** with a sub-bass hit. No music: voice plus a few precise SFX.

## 2. Edit grammar (cutting)

| Rule | Measured in reference |
| --- | --- |
| Jump-cut every dead gap; keep breaths under 0.1 s | cuts at 3.13, 4.40, 6.20, 8.10, ~14.0 s. The audio floor drops to −75 dB right at each cut (hard cut, no room tone) |
| Average shot ≈ 2–3 s; never hold an un-dressed frame longer than ~1.5 s | 6 shots in 16.9 s |
| Same framing on A-roll (medium close-up, eyes at ~22 % height, chest at 55 %) | no punch-in/out between A-roll jump cuts. The cut itself is the energy |
| One B-roll insert at the "pain" line, shot on set (mic + camera in frame, subject grimacing) | 6.20 → 8.10 s |
| Transitions are **masks for the jump**, never decoration: blur-through (most cuts) and one stripe flash (the big turn) | see §6 |
| Caption groups change on the cut, not mid-shot | every group exits at or before its cut |

## 3. Typography

**Fonts (shipped in `assets/fonts/`, all OFL):**

- **Hero + lead/tail words: Inter 900** (reference is a Helvetica Now Display / Inter Display Black
  style heavy grotesk). Tight tracking `letter-spacing: -0.045em`, `line-height: 0.86`.
- Small white words: Inter 800, `-0.03em`.
- UI text (alert cards, chat pill): **Sora 400**, `-0.04em` (wide geometric, light weight).
- REC label / tiny UI: Inter 800, uppercase, `0.02em`.

**Three tiers (sizes at 1080 w):**

| Tier | Role | Size | Color |
| --- | --- | --- | --- |
| `hero` | the one word that carries the line (`Prospects`, `Understand`, `Content`, `Camera Stresses`, `You record`, `Your plate`) | **150–165 px**. Hero line spans **75–82 % of frame width** (≈ 820–880 px). Shrink the font size until the line fits, never wrap | lime `#DCF850` + glow |
| `lead` | connector words before the hero (`If the`, `to`, `your`, `being on`, `even if`) | **0.38–0.55 × hero** (60–85 px) | warm white `#F8F8F0` |
| `tail` | the words after it (`meet you`, `your value`, `is failing`, `you out`, `you are unsure`) | same as lead. One word in the tail may go **lime** for a second accent (`your **value**`, `you **out**`) | white, optional lime |

**Stack geometry (the signature):**

- The hero line sets the block width. Lead line is **left-aligned** to the hero's left edge, or
  **split** (`If the ··· have to`, first chunk left, second chunk right). Tail line is
  **right-aligned** to the hero's right edge. The result is a zig-zag that reads top-left → hero → bottom-right.
- Lines overlap: lead/tail sit **tight** on the hero (negative gap ≈ −0.08 × hero size), so
  descenders/caps nearly touch. Never a loose paragraph.
- Hero is always Title-Case (`Understand`, `Content`, `Your plate`). Small words lowercase.
- Only one hero per screen. Two-word heroes stay on one line (`Camera Stresses`).

**Text finish:**

- Lime words glow: `text-shadow: 0 0 22px rgba(220,248,80,.55), 0 0 60px rgba(220,248,80,.22), 0 6px 18px rgba(0,0,0,.55)`.
- White words: soft dark lift only, plus a faint halo: `0 0 14px rgba(255,255,255,.18), 0 4px 14px rgba(0,0,0,.6)`.
- No outlines, no boxes behind captions, no emoji in captions.

## 4. Palette (pixel-sampled)

| Token | Hex | Use |
| --- | --- | --- |
| `--lime` | `#DCF850` | hero words, arrow icon, secondary accent word |
| `--white` | `#F8F8F0` | lead/tail words, UI text (slightly warm, never pure `#FFF`) |
| `--red` | `#E8001F` | strikethrough, REC dot, warning icon |
| `--ring` | `#E2D0BE` | focus ring around face on B-roll (warm cream) |
| `--pill-a / --pill-b` | `#B06858` → `#904840` | chat pill (terracotta, lighter at top) |
| `--card-edge / --card-core` | `#120808` → `#3A0008` | alert-card fill: black edges, deep red glow from the bottom centre |
| `--ink` | `#000` | bottom fade |

Footage look (the grade was baked in at source, so don't fake it with CSS filters): low-key,
average luma ≈ 50/255, crushed blacks, desaturated cool gray wall with warm skin, one warm
practical (orange abstract art) top-left. The bottom **12–15 % fades to pure black** (a framing
gradient you *can* add: `linear-gradient(to top, #000 0%, rgba(0,0,0,.85) 8%, transparent 22%)`),
which also gives contrast to anything placed low. If footage needs regrading, go through
`/media-use` → `references/media-treatments.md`.

## 5. Placement map (9:16, 1080×1920)

| Zone | Center Y | When |
| --- | --- | --- |
| **Chest** (default) | **54–58 %** (y ≈ 1040–1110) | every A-roll caption. Sits on the torso, under the chin, over the hands |
| **Head-top** | **12–17 %** (y ≈ 230–330) | when the lower frame is busy (B-roll with mic/camera) or the line is the thesis |
| **Behind the head** | 15 % | thesis word (`content matters`): giant lime word **composited behind the subject** (needs a matte: `/embedded-captions` `matte.cjs`). Use once per video at most |
| UI cards | 56 % and 66 % | alert toasts stacked under each other, ~62 % frame width, centred |
| REC frame | corner brackets inset 75 px from the sides, 130 px from top / bottom | the "recording" beat |

Never cover eyes/mouth. Horizontally the block is centred, but it may drift ±40 px to clear a hand or a prop.

## 6. Motion spec (GSAP, seek-safe)

**Word entry: "focus-in"** (every word, on its spoken onset):

```js
// hero: snaps in big and sharp-ish, settles fast
tl.fromTo(w, {opacity:0, scale:1.22, filter:"blur(10px)"}, {opacity:1, scale:1, filter:"blur(0px)", duration:0.16, ease:"power3.out"}, t);
// lead/tail: softer ghost fade (reads "ghosted" for ~2 frames)
tl.fromTo(w, {opacity:0, scale:1.06, filter:"blur(6px)"}, {opacity:1, scale:1, filter:"blur(0px)", duration:0.14, ease:"power2.out"}, t);
```

Words appear **one by one on the voice**, with no karaoke recolor afterward. Text never moves once
it has landed, apart from that settle. Static type after the pop is part of the look.

**Group exit: blur-out**, synced with the footage blur at the cut:
`tl.to(stack, {opacity:0, filter:"blur(14px)", scale:1.04, duration:0.18, ease:"power2.in"}, cut-0.18)`.

**Props:**

| Prop | Look | Motion |
| --- | --- | --- |
| **Strikethrough** | red `--red` bar, 8 px, rounded, extends ~6 % past the word each side, rotated −4°, faint red glow | draws left→right (`scaleX 0→1`, 0.22 s, `power2.out`) ~0.3 s after the hero lands, *before* the tail says why (`is failing`) |
| **Arrow cursor** | lime outline paper-plane / cursor glyph, 3 px stroke, glow, ~60 px | flies in from bottom-left with rotation (`x:-80,y:90,rotation:-120 → 0`, 0.4 s, `back.out(1.6)`), lands left of the tail line |
| **Focus ring** (B-roll) | 4 px `--ring` circle, settles at ≈ **640 px diameter (59 % width)** centred at y ≈ 770 (40 %), under the top caption. Outer glow `0 0 24px rgba(226,208,190,.6)` | scales **in from 1.35 → 1** with fade, 0.3 s `power3.out`, on the cut. Under it the B-roll does a **punch-out 1.15 → 1.0** over 0.5 s |
| **Chat pill** | terracotta gradient pill, Inter 500 34 px white, 1 px light border, small dot "tail" bottom-left | sits on the ring's upper-right edge (never over the caption), pops in (`scale .6→1`, `back.out`), text types **word by word** |
| **REC viewfinder** | white 3 px L-brackets (arms 90 px) in all four corners, `● REC` top-left (dot `--red`), small `+` crosshair bottom-right | brackets fade in 0.2 s; REC dot blinks (1 s period, finite repeats) |
| **Red dot "period"** | 22 px `--red` dot placed after the hero `record` like a recording light | pops with the beep SFX |
| **Alert cards** | 670×120 px, radius 30, fill = radial red glow from the bottom centre over near-black, 1.5 px `rgba(255,255,255,.12)` border, icon left (red ⚠ triangle / 💸), Sora 400 46 px white | rise + blur in (`y:30, blur 12px → 0`, 0.25 s); text types **word by word**; 2nd card stacks 140 px below ~1 s later |

**Transitions:**

1. **Blur-through cut** (default): footage wrapper `filter: blur(0→16px)` over the last 0.12 s
   before the cut, then `16px→0` over 0.15 s after it; captions blur-out at the same time.
2. **Stripe flash** (once, on the biggest turn of the script): full-frame vertical white stripes
   (`repeating-linear-gradient(90deg, #fff 0 7px, transparent 7px 16px)`) plus a white wash.
   Opacity 0 → 1 → 0 over **0.35 s** (peak at the cut), luma spikes to ~75 % white. Stripes slide
   40 px sideways during it. Pair with whoosh-in + sub boom.

## 7. Sound design (no music)

Measured: no BGM at all. The noise floor hits −75 dB on every cut. Voice carries the piece; SFX are sparse and exact.

| Moment | SFX | Level |
| --- | --- | --- |
| first hero word lands (0.3 s) | bright **shimmer/chime** (tones at ~3, 5.8, 7.6, 17.6 kHz, ~0.6 s) | −18 dB under voice |
| blur-through cut into the problem line (3.13 s) | **low impact / sub hit** + air | peaks −18 dB in the sub band |
| stripe flash (4.0–4.6 s) | **pitch-sweep whoosh** into **sub boom** at the flash peak | the loudest SFX, ≈ −15 dB sub |
| REC red dot (9.09, 9.14 s) | **double beep**, ~3.5 kHz, 2 × 40 ms | −20 dB |
| alert cards | soft UI "pop" / notification tick on each card (optional) | −22 dB |

In this repo: `assets/sfx/whoosh-short.mp3` and `assets/sfx/sparkle.mp3` exist. Resolve the boom,
beep and UI pop through `/media-use` (`resolve sfx …`). Every `<audio>` needs an `id`.

## 8. Script / beat structure the style expects

The reference script is a classic agency hook. The style is built for this rhythm:

1. **Hook / condition** (0–3 s): `If the Prospects have to meet you / to Understand your value`
2. **Problem** (3–4.4 s): `your Content is failing`, with the hero struck out
3. **Turn** (stripe flash) (4.4–6.2 s): `You know content matters`, thesis behind the head
4. **Pain, shown** (B-roll + ring + pill) (6.2–8.1 s): `being on Camera Stresses you out`
5. **Objections as UI** (REC frame + error toasts) (8.1–13.9 s): `even if You record you are unsure` → `what to say?` / `how it turn to revenue?`
6. **Offer / resolve** (14–16.9 s): `we take it off Your plate`, plain, no props (the calm *is* the resolution)

Each beat gets **one** new prop. Never reuse a prop in the next beat.

## 9. Build it in HyperFrames

1. Load `/hyperframes-core` (contract). For a transcript: `npx hyperframes transcribe` (needs
   whisper-cpp, not installed here) or reuse `transcript.json`.
2. Copy `templates/lime-pop.html` → project `index.html` (or a sub-composition), and
   `assets/fonts/*` → project `assets/fonts/`.
3. Edit the `GROUPS` data: per word `[text, onsetSeconds, tier?]`. Tiers are `hero`, `lime`
   (accent in a small line), or default white. A `"|"` entry is a flexible spacer (for split lead
   lines). `place: "chest" | "top"`. `props` lists the per-beat UI props with their times.
4. Set `CUTS` (jump-cut times → blur-through) and `FLASH` (the one stripe flash). Set `FACE`
   (face centre in the footage, 1080×1920 space) and `RING`. The stand-in insert punches in by
   `INSERT_SCALE` and moves the face to the ring centre. Swap in a real B-roll clip when you have one.
   Caption words carry `data-layout-allow-overlap` because the tight stack overlaps on purpose.
   Any *other* overlap (pill on caption, card on caption) is a real collision, so check snapshots.
5. Text behind the head: run `/embedded-captions` matte step and layer the matte video above the
   word. Otherwise use `place:"top"` (the template does this).
6. `npm run check` → fix everything → `npx hyperframes snapshot --at <beats>` and compare with the
   reference frames → `npm run render` after approval.

## 9b. Bright / high-key footage (learned on the "AI photo shoots" edit)

The reference is shot dark. On a white wall or light clothing, lime has almost no contrast. Don't regrade
the person dark (that's a stylization the footage didn't ask for). Instead:

- Keep the palette and give every caption word a **dark halo** instead of the glow-only shadow:
  white words `0 0 3px rgba(0,0,0,.55), 0 2px 10px rgba(0,0,0,.6), 0 0 34px rgba(0,0,0,.45)`, lime
  words the same plus a faint lime glow `0 0 22px rgba(220,248,80,.35)`.
- Place chest captions under the chin of *this* subject (≈ 65 % height when the chin sits at 52 %).
  Avoid the head-top zone if it's a bright wall.
- HUD text on a bright wall (`● REC`) gets a small dark capsule backing (`rgba(0,0,0,.55)`, radius 10), and
  brackets get a soft dark drop-shadow.
- Keep bass hits short (≤ 0.8 s, volume ≈ 0.3) so their tail doesn't fill the speech gaps after the cut.



- ✅ one lime hero per screen; small words white; tight, edge-pinned stack
- ✅ words land on the voice onset (±1 frame); groups die on the cut
- ✅ one new UI prop per beat; props carry *meaning* (strike = failing, REC = recording, toasts = doubts)
- ✅ silence-free jump cuts masked by blur-through; one stripe flash max
- ❌ no music bed, no constant whoosh on every cut, no karaoke recolor, no caption boxes
- ❌ no pure `#FFF` text, no second accent colour beyond lime + red (+ terracotta pill)
- ❌ don't cover the face; don't wrap a hero line; don't animate text after it settles
- ❌ don't copy the reference's footage, B-roll or the AI-generator ✦ mark visible bottom-right of its B-roll
