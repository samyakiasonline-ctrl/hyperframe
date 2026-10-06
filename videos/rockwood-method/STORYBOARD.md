# Storyboard: The Rockwood Method promo

## Round 1 (2026-10-06): review and explainer edit (motion graphics, on-screen text, SFX)

### Source

- `assets/source.mp4`: 27.6 s, 720×1280, 25 fps, one locked-off take. A presenter at a desk
  (laptop on the left, podcast mic on the right, maroon backdrop) pitches "The Rockwood Method".
  `assets/speaker.mp4` is a 1080×1920 re-encode with a keyframe every second.
- Script (`transcript.json`, word-level): "Think finance tools are just for Wall Street bros?
  Imagine budgeting with a potato. Enter the Rockwood Method: self-guided, downloadable finance
  magic. The Rockwood Financial Playbook, Printable Planner Bundle, and AI Income Optimizer, each
  a game changer. Build a rock-solid financial foundation, no hand-holding needed. 100%
  self-guided, zero hassle. Life post-Rockwood: less stress, more savings. Grab yours now at
  rockwoodmethod.com/shop. Don't sleep on this."
- Transcription ran offline: Moonshine base-en for the text, and pocketsphinx forced alignment
  for timings. A verifier confirmed each disputed phrase. She says "dot com shop", with no "slash".

### Review: what could be better in the original

1. **Nothing on screen.** The brand, the three products, the benefits and the URL exist only in
   the audio, so muted feed viewers get a woman talking with no visible topic.
2. **Weak hook.** The first 2 s look like the other 25 s, and the hook and the potato joke only
   work with sound on.
3. **The CTA is never shown.** The URL is spoken once in about 1.4 s at her fastest pace, and the
   last line is 3–5 dB quieter than the rest.
4. **The products are named, not shown.** Three names pass in 4.4 s with 0.1 s gaps and no
   explanation or visuals.
5. **One flat shot for 27.6 s.** There are no cuts, zooms or layout changes.
6. **Voice only.** There's no sound design, and the gaps between sentences are gated to dead
   silence.
7. **1.6 s of silence** after the last word, while she holds a pose and winks.
8. **Footage limits, which can only be mitigated:**
   - a 30→25 fps conversion drops one frame in five, which shows as judder on fast gestures;
   - a soft 720p social re-encode, upscaled 1.5×;
   - banding in the backdrop gradient;
   - a dull 64 kb/s HE-AAC voice with plosive thumps (9.15, 10.08, 13.77, 20.09 s).
9. **The script repeats one idea four times** ("self-guided", "no hand-holding", "100%
   self-guided", "zero hassle").
10. **Promo basics missing:** no logo, product visuals, offer or handle. The claims ("AI Income
    Optimizer", "100%", "more savings") need careful, non-promissory visuals.
11. **Publishing questions:**
    - the file was downloaded from a social account through ssspin.io, so rights and the
      presenter's consent are unconfirmed;
    - it's unknown whether the presenter is AI-generated;
    - any paid partnership needs disclosure;
    - the exact URL needs confirming.

### Edit plan (beats; times in seconds)

| #   | Time        | Beat                                      | Picture                                                                                                                         |
| --- | ----------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1   | 0.00–2.29   | Hook                                      | Top band, visible on frame 0: "Think finance tools are just for" over **WALL STREET BROS?**; each word pulses gold as spoken; cream marker strike 2.05–2.29 |
| 2   | 2.29–4.15   | Joke                                      | "Imagine" over **budgeting with a *potato*.**; flat SVG potato wired to a tiny calculator drops into the lower stage at 3.50 |
| 3   | 4.15–5.57   | Reveal                                    | Top-band wordmark THE *Rockwood* METHOD (mask reveal on "Rockwood" 4.60–5.02); camera eases to 1.06×                          |
| 4   | 5.57–7.99   | Format                                    | Chips SELF-GUIDED / DOWNLOADABLE (download arrow) / FINANCE MAGIC (sparkle at 7.57)                                             |
| 5   | 7.99–13.62  | Products (split)                          | Footage moves up, cream panel below: wordmark header + 3 cards (Financial Playbook, Printable Planner Bundle, AI Income Optimizer) + GAME CHANGER stamp |
| 6   | 13.62–15.80 | Foundation                                | **ROCK-SOLID** / financial foundation; three stone blocks stack in the left column                                              |
| 7   | 15.80–17.25 | Independence                              | **NO HAND-HOLDING** / needed.; two-hands icon pulls apart in the right column                                                   |
| 8   | 17.25–19.57 | Callback                                  | SELF-GUIDED chip returns with a gold **100%** stamp; **ZERO HASSLE** with a drawn check; camera at 1.12×                         |
| 9   | 19.68–22.50 | Outcome                                   | Header LIFE POST-*Rockwood*; lower-stage card: LESS STRESS (taupe bar shrinks), MORE SAVINGS (gold bar grows), no numbers       |
| 10  | 22.50–24.98 | CTA (split)                               | **GRAB YOURS NOW**; URL card `rockwoodmethod.com` + `/shop` pill, highlighter in sync with her words, cursor clicks the pill     |
| 11  | 24.98–25.95 | Urgency                                   | **DON'T SLEEP ON THIS** with an alarm-clock icon; the URL stays put                                                             |
| 12  | 25.95–27.60 | End hold                                  | Wordmark + URL hold; one shine across the URL; the pill pulses once                                                             |

Sound: 20 cues from the bundled Pixabay library, each placed in a measured speech gap with its
own level, on one SFX bus with a limiter. The voice gets a 100 Hz high-pass for the plosives and
+3 dB on "Don't sleep on this". No music bed.

Guardrails:

- No `$`, rising income charts or count-ups.
- "100%" appears only as part of "SELF-GUIDED".
- All three products get equal weight.
- Nothing is invented: no prices, offers, handles or disclaimers.

### Open decisions (defaults in use)

- **Rights.** Built as a draft; it shouldn't be published until rights are confirmed.
- **URL.** Shown as `rockwoodmethod.com/shop`.
- **Assets.** Type-only wordmark, since there are no logo or product mockups.
- **Disclosures.** Nothing burned in.
- **Captions.** No word-by-word captions on screen, because the key-phrase graphics carry her
  words; `captions.srt` is delivered for platform captions.
- **Music.** No music.
