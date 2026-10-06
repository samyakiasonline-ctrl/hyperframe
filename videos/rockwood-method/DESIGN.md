# Design contract: The Rockwood Method promo

Every scene file follows this contract, so scenes built separately read as one film.
Canvas: 1080×1920, 25 fps, 27.6 s. Coordinates are canvas pixels.

## Type

| Role            | Font                                      | Notes                                       |
| --------------- | ----------------------------------------- | ------------------------------------------- |
| Headline / slam | Montserrat 900, caps                      | 64–96 px; letter-spacing −0.01em            |
| Body / lines    | Montserrat 800                            | 40–64 px                                    |
| Kicker / labels | Montserrat 700, caps, letter-spacing 0.18em | 26–32 px                                  |
| Accent word     | Instrument Serif italic                   | the "Rockwood" wordmark and one accent word |

Wordmark (a type-only placeholder, not the client's logo): small caps **THE** (Montserrat 700,
letter-spacing 0.2em), then **Rockwood** (Instrument Serif italic), then **METHOD** (Montserrat 700).
Set "Rockwood" this way every time it appears.

`@font-face` sources, written root-relative exactly like this in every file:

```css
@font-face { font-family: "Montserrat"; src: url("assets/fonts/montserrat-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-display: block; }
@font-face { font-family: "Montserrat"; src: url("assets/fonts/montserrat-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-display: block; }
@font-face { font-family: "Montserrat"; src: url("assets/fonts/montserrat-latin-900-normal.woff2") format("woff2"); font-weight: 900; font-display: block; }
@font-face { font-family: "Instrument Serif"; src: url("assets/fonts/instrument-serif-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: block; }
@font-face { font-family: "Instrument Serif"; src: url("assets/fonts/instrument-serif-latin-400-italic.woff2") format("woff2"); font-weight: 400; font-style: italic; font-display: block; }
```

## Colour

| Token  | Hex       | Use                                                                          |
| ------ | --------- | ---------------------------------------------------------------------------- |
| cream  | `#FFF4E6` | type on the wall; card and panel fills                                       |
| ink    | `#2A1714` | type and icons on cream                                                      |
| gold   | `#D9AD6C` | accents: large type on the wall, fills, strokes, stamps (never small text on cream) |
| taupe  | `#9C8579` | muted element (the "stress" bar), secondary lines on cream                   |
| wall   | `#522F29` | the backdrop's measured colour, for reference only                           |

No saturated red or pink. No dark strokes or shadows on the wall: type on the wall is cream or
gold with at most a soft shadow (`0 2px 12px rgba(0,0,0,.35)`). Cards are opaque cream with a
radius of 28–36 px and a soft shadow (`0 14px 40px rgba(0,0,0,.28)`).

## Layout (where things may sit)

- **Face and hair, keep out:** x 320–830, y 357–900. Camera push-ins raise the head top to about
  y 331 at 1.12×.
- **Right rail, keep out** (platform buttons): x > 940, y 850–1650.
- **No text below y 1440** (platform caption and username UI). Panel *fill* may run to the bottom.
- **Top band** (main text slot on full-frame beats): x 60–1020, y 170–335. Cream or gold type sits
  directly on the wall, with no card. At most 2 lines, at most 880 px wide. During 17.05–19.60 the
  camera is at 1.12×, so text must end by y 315.
- **Side columns**, for small icons only: left x 70–290, y 600–880; right x 840–1000, y 400–720.
- **Lower stage:** x 60–940, y 1060–1440. Opaque cream cards only, and only briefly, because
  her hands live here.
- **Split panel** (products 7.99–13.62; CTA 22.50–27.60): the root moves the footage up 180 px,
  so her face sits at about y 186–720. A cream panel covers y 960–1920. Content goes inside
  x 60–940, y 985–1440. The top band is NOT available during a split (her face is there).

## Motion

- GSAP only, one paused timeline per scene: `window.__timelines["<composition-id>"] = tl`.
- Times inside a scene are **local**: local = global − the host's `data-start`. Quantize
  to 1/25 s: `Math.round(t * 25) / 25`.
- Entrances lead their word by 1–3 frames (0.04–0.12 s) and take ≤ 0.25 s. At most 5 new words
  per graphic. Swap graphics inside the measured speech gaps: 2.28–2.43, 4.10–4.23, 7.99–8.14,
  9.55–9.68, 10.96–11.04, 12.47–12.60, 13.52–13.77, 17.03–17.26, 19.58–19.78, 20.90–20.97,
  21.64–21.74, 22.50–22.74, 24.89–25.03.
- Eases: `power3.out` for entrances, `power2.in` for exits, `back.out(1.6–2.2)` for pops and stamps.
- Nothing flashes more than 3 times per second. Wobbles stay at or below 3 Hz.
- Word timings live in `transcript.json`, with acoustic corrections already applied.

## File contract (lint enforces most of this)

- The scene file is `compositions/<id>.html`: `<template>` wrapping `<style>`, then
  `<div id="root" data-composition-id="<id>" data-width="1080" data-height="1920">`, then `<script>`.
  Style the root as `#root { position:absolute; inset:0; }`, never by class.
- Prefix every element id with the scene id (`hook-title`, `prod-card-1`), so ids are unique
  across the assembled page.
- No external URLs or CDNs. `gsap` is already global (the root loads `assets/vendor/gsap.min.js`).
- Asset paths are root-relative (`assets/...`), never `../assets/...`.
- Use `fromTo` for entrances. Never tween `visibility`, `display` or `autoAlpha`. Hide
  initial states with `fromTo` (immediateRender), not `tl.set(..., 0)`.
- SVG strokes with round caps paint a dot even at full dash offset, so keep them at
  `opacity: 0` until their draw starts. Give any path you measure with `getTotalLength()` a
  static `d` attribute in the HTML.
- No `Math.random`, `Date.now`, network calls, `<br>` in body text, or CSS `transform` on
  elements GSAP also transforms. Deterministic only.
- Do not touch `index.html`, other scenes, or anything outside your own file and scratch dir.
