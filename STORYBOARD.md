# Storyboard: "You are allowed to reinvent yourself"

## Round 2 (2026-10-06): explainer edit with motion graphics, typography, and SFX

### What the source is

- `assets/source.mp4`: 16.5s, vertical 720×1280, 25 fps, one continuous talking-head take
  (man at a podcast mic, wood-slat wall). Speech ≈ −14 LUFS integrated, so loudness is fine for social.
- Script: three permissions ("You are allowed to **reinvent** yourself / **outgrow** old patterns /
  become more **confident**"), a thesis ("Your **past** does not have to define your **future**"),
  and a closer ("**Growth** is possible at any stage of life").

### Review: what could be better in the original

1. **Two visible morph glitches.** At ~5.7–6.0s and ~12.5–12.7s the footage morphs between two
   framings: clasped hands melt into open hands and the mic stand fades in. These look like
   AI-generated or morph-cut transitions and are the most distracting thing in the clip.
2. **No visual structure.** The script is a list of three permissions plus a thesis, but nothing
   on screen shows that structure, so it reads as one undifferentiated 16s shot.
3. **No hook in the first second.** The first frame looks like every other frame, so nothing stops
   a scroll.
4. **Static camera for 16s.** There are no punch-ins, so the key line ("past ≠ future") gets no
   extra weight.
5. **Silent apart from the voice.** There are no SFX, no transitions, and no music bed.
6. **Abrupt ending.** It stops on "life." with no hold, quote, or recap that would make it worth
   saving or sharing.
7. **Low resolution.** 720×1280 at about 0.9 Mb/s, with 64 kb/s audio. It upscales acceptably but
   stays soft, so keep punch-ins modest.
8. **Previous caption pass.** It named Montserrat without loading it (it fell back to a system
   font), and every word had the same weight.
9. **Rights.** The file came from a Pinterest downloader (Klickpin). Confirm you have the right to
   republish this footage before posting it.

### What this edit does

| Time        | Beat                                         | Picture                                                                                                                                 | Sound                                                       |
| ----------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 0.0–9.7     | "You are allowed to…" ×3                     | Top band: **YOU ARE ALLOWED TO** + three numbered chips; each fills gold with a drawn tick on its spoken keyword (0.92 / 3.40 / 7.48s) | whoosh in, pop per unlock, soft chime when all three are on |
| 5.5–6.2     | morph glitch 1                               | warm **camera-flash cut** (adapted from the registry `editorial-flash-overlay`); camera reset hidden under it                         | whoosh                                                      |
| 9.45–12.75  | "Your past does not have to define your future" | camera **punch-in** to 1.13×; **Past ≠ FUTURE**: "does" draws =, "not" slashes it into ≠, "future" pops in gold                      | whoosh + bass impact, clicks, pop, sparkle                  |
| 12.28–12.98 | morph glitch 2                               | second flash cut, camera resets to wide                                                                                                 | whoosh                                                      |
| 12.55–16.5  | "Growth is possible at any stage of life"    | **growth line** drawing across ages 20 → 80+, rising through small dips                                                                 | riser that crests into the end card                         |
| 16.1–18.4   | end card                                     | cream sheet wipes up: "Growth is possible / *at any stage* / of life." + recap chips (Reinvent · Outgrow · Confident)                   | whoosh, chime, three soft clicks                            |

Captions run throughout. They're word-synced karaoke in Montserrat 800, and the key words
(reinvent, outgrow, confident, past, future, Growth, any stage) are set in gold Instrument Serif
italic.

### Files

- `index.html`: root. Holds the footage in a `#cam` wrapper (camera moves), the shades, the scene
  hosts, and every SFX `<audio>`.
- `compositions/permissions.html`, `thesis.html`, `growth.html`, `end-card.html`: one per beat.
- `compositions/flash-cut-1.html`, `flash-cut-2.html`: the glitch-hiding transitions.
- `compositions/captions.html`: the single caption track.
- `assets/speaker.mp4`: 1080×1920 lanczos upscale of `source.mp4` with a keyframe every second
  (the original has one every 2s, which can freeze on seek).
- `assets/fonts/`: Montserrat and Instrument Serif (OFL). `assets/sfx/`: Pixabay-licensed SFX
  (see `CREDITS.md`).

### Open options for the next round

- **Music bed.** No offline music source is available here. Signing in to HeyGen
  (`heygen auth login --oauth`) unlocks the music catalog, or supply a track. A soft, uplifting
  piano bed at about −18 dB under the voice would suit this.
- **Hook card.** Optionally prepend a 0.6s title ("3 permissions you need to hear") before the
  first word.
- **CTA.** The end card says "A REMINDER". Swap it for your handle or a call to action if you have
  one.
