# Design contract: Xylazine explainer

Every composition file follows this contract. The full beat plan is the edit brief in `STORYBOARD.md`.
Canvas: 1080×1920, 30 fps, 8.2 s. Coordinates are canvas pixels.

## Look: sober and clinical (educational topic)

| Token        | Value                                    | Use                                             |
| ------------ | ---------------------------------------- | ----------------------------------------------- |
| plate        | `#0C1715` at 88% opacity, radius 28, hairline border `rgba(255,255,255,.08)`, shadow `0 8px 24px rgba(0,0,0,.35)` | the one graphics plate |
| text         | `#F7F5F0`                                | all text on the plate and the captions          |
| text-dim     | `#F7F5F0` at 62%                         | secondary text ("or", the docked headline)      |
| accent amber | `#F2A33A`                                | key terms, underline, slots, stamp fill         |
| chip         | `#F7F5F0` fill, `#111` text              | UNCONSCIOUS / CALM chips                        |
| stamp        | `#F2A33A` fill, `#111` text              | VETERINARY DRUG                                 |

No red, no flashing, no hazard or "breaking" styling, no scrims, gradients, blur or vignette over the
footage. The footage pixels are never treated.

## Type

Montserrat only. Use 900 for the name and the stamp, and 800 for the headline, chips and captions.
ALL CAPS only on key-term graphics. Minimum sizes: captions 60 px, chips 44 px, smallest text 36 px.

```css
@font-face { font-family: "Montserrat"; src: url("assets/fonts/montserrat-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-display: block; }
@font-face { font-family: "Montserrat"; src: url("assets/fonts/montserrat-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-display: block; }
@font-face { font-family: "Montserrat"; src: url("assets/fonts/montserrat-latin-900-normal.woff2") format("woff2"); font-weight: 900; font-display: block; }
```

## Layout (at camera 1.0×; the camera zooms up to 1.16× about the origin 565, 870)

- **Graphics plate** (the only plate): x 70–1010, y 230–570. Content box with 36 px padding:
  x 106–974, y 266–534. Rows: A y 266–330, B y 344–454, C y 468–534. Nothing above y 220
  (platform header) or below y 575. Her head top is at y 628–648 (about 589 at 1.16×).
- **Caption band**: centred on x 540 inside x 120–940; one line within y 1400–1490. The C4 chunk
  may take two lines (y 1380–1510). The band sits over the black sweater, where white text is
  about 17:1.
- **No text**:
  - face: x 405–700, y 700–1050;
  - gesture zone: x 180–950, y 960–1380;
  - light glint: x 830–870, y 945–1000;
  - platform UI: y < 220, y > 1520, x > 940 for y 850–1700, and x < 60.
- Hands cross the caption band at 1.80–1.95 s and 4.47–4.65 s, so caption text gets
  `text-shadow: 0 0 2px rgba(0,0,0,.9), 0 2px 12px rgba(0,0,0,.6)`.

## Motion

- GSAP, one paused timeline per composition, registered as `window.__timelines["<id>"]`.
- Entrances: 0.18–0.30 s with `power3.out`. Exits: 0.15–0.20 s with `power2.in`.
- The only overshoot is the stamp (`back.out(1.4)`). No bounce, elastic, shake or scramble. Repeats are finite.
- Times come only from `transcript.json` (verified, 27 words). Composition times equal global times:
  both scene hosts start at 0.
- Nothing flashes more than 3 times per second.

## Content guardrails

- Claims are limited to her words: the name XYLAZINE, ANIMALS, UNCONSCIOUS / CALM (her
  "behosh ya shaant"), VETERINARY DRUG, and her question.
- None of the following:
  - anything about human use, street names, fentanyl, overdoses, antidotes, doses or statistics;
  - "only for animals";
  - pills, syringes, vials, powder, smoke or slumped figures;
  - comic knocked-out stars;
  - a pronunciation chip;
  - any CTA, handle or "Part 2".
- Icons: one inline-SVG paw, and a vet badge (the paw in a rounded shield with a small plus).

## File contract (lint enforces most of this)

- Each composition is `compositions/<id>.html`: a `<template>` wrapping `<style>`, then
  `<div id="root" data-composition-id="<id>" data-width="1080" data-height="1920">`, then `<script>`.
  Style the root as `#root { position:absolute; inset:0; }`.
- Prefix every element id with the composition id. No external URLs. `gsap` is global. Asset paths
  are root-relative (`assets/...`).
- Use `fromTo` for entrances. Never tween `visibility`, `display` or `autoAlpha`. Hide initial states with
  `fromTo` (immediateRender), not `tl.set(..., 0)`.
- Dash-offset line draws need `autoRound: false` (GSAP rounds px otherwise and the draw jumps).
  Round-cap strokes stay at `opacity: 0` until their draw starts. Any path you measure needs a static `d`.
- No `Math.random`, `Date.now` or network calls, no `<br>` in body text, and no CSS `transform` on
  GSAP-tweened elements.
- Edit only your own file.
