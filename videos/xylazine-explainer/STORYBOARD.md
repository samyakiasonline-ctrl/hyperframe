# Storyboard: Xylazine explainer (Hinglish talking head)

## Round 1 (2026-10-07): review and explainer edit (motion graphics, on-screen text, SFX)

### Source

- `assets/source.mp4`: 7.47 s, 2160×3840 at 29.97 fps, one locked-off 4K take: a presenter at a
  marble desk in front of a teal backdrop, with an orange lamp and plants.
  `assets/speaker.mp4` is a 1620×2880 30 fps proxy, which allows sharp punch-ins up to about 1.3× on the 1080×1920 canvas.
  `assets/hold-f222.mp4` is a still of frame 222, the last clean frame.
- Speech is Hinglish, transcribed offline with multilingual Whisper-small. A verifier confirmed the words and timings
  acoustically (`transcript.json`, 27 words):
  "Lekin ye drug actually karta kya hai? Iska naam hai Xylazine, jo animals ko behosh ya shaant karne ke liye di
  jaane wali ek veterinary drug hai." In English: "But what does this drug actually do? It's called Xylazine: a veterinary drug
  given to animals to make them unconscious or to calm them down."

### Review: what could be better in the original

1. **One-frame flash cut to a different take on the very last frame** (Proxy frame 223 = 7.433-7.467 s (source 7.441-7.474 s)). The final frame is a different take: her face shifts right, a hand jumps up and her mouth is open. Frame-to-frame luma difference jumps to 12.4, against 0.7-1.1 on the frames before it; the largest change anywhere else is 5.5, at the 1.9 s gesture. I re-measured this on the proxy: frame 223 diff 12.41, max elsewhere 5.52. On a looping Reel it flashes once per loop and reads as a glitch.
2. **Muted viewers get nothing: no on-screen text and one locked-off shot** (0.00-7.47 s). The drug's name, what it does and what kind of drug it is exist only in the audio. The source has no text and no cuts (mean frame difference 0.017 at 10 fps), and most feed viewing starts muted.
3. **The cold open is a fragment ('Lekin ye drug...') and the name arrives 34% of the way in** (0.11-2.545 s). It opens on 'Lekin' ('But') and 'ye drug' ('this drug'), which point back to a sentence that is not in the clip. The drug is not named until 2.545 s. 'Lekin' cannot be trimmed cleanly: the quietest point before 'ye' is -18.7 dBFS, against -52 dBFS silence.
4. **The voice is mastered far too hot (-7.6 LUFS, +0.2 dBTP) and brickwall-limited** (Whole clip; peaks above 0 dBTP at 0.18, 4.1 and 7.2 s). It sits 6.4 LU above the -14 LUFS social target, and its peaks touch full scale: 45 of 374 20-ms blocks are within 0.25 dB of it. Any sound effect added on top would clip, and the +0.2 dBTP peaks will clip again when the platform re-encodes to AAC. Otherwise the recording is clean: no clipping, no rumble, and the noise floor is 43-46 dB below the speech.
5. **Abrupt ending with no time to take in the answer** (7.27-7.474 s). 'hai.' ends at about 7.42-7.44 s, and the file ends 30-50 ms later (video 7.474 s, audio 7.488 s). A muted viewer gets under 0.1 s after the last idea, and the flash frame on top makes the ending look like a glitch.
6. **Static, loose framing: a small subject under a third of empty wall** (0.00-7.47 s). The top of her head is at y 628-648 of 1920, so the top third of the frame is wall. Her face is about 250x340 px, roughly 18% of the frame height. The camera does not change for 7.5 s.
7. **Very fast, continuous delivery** (0.11-7.44 s; only pause 1.74-1.93 s). She speaks at about 3.7 words/s (about 221 wpm), around 6.1 syllables/s. The only pause is 1.74-1.93 s, and the second sentence runs 5.5 s without a break. Several words last only 65-130 ms. Word-by-word captions would flicker, and mid-frequency sound effects under words hide consonants: in the audio simulation, a whoosh peaking at 0.10 s cut the audibility of the start of 'Lekin' to 0.47.
8. **Background clutter pulls the eye away from her face** (Whole clip). The orange lamp at eye level (x 0-265, y 765-945) is the most saturated thing in the frame: chroma 89.5 against about 31 for her face. Also distracting: the flowers, the lamp tripod, a light glint behind her shoulder (x 830-870, y 945-1000) and her hands reflected in the glossy desk.
9. **The wall behind her makes plain white text unreadable** (Whole clip). White text measures only 1.3-2.0:1 contrast over the cream hotspot behind her head and 2.5-3.7:1 over the teal wall. Only y < 150 and the black sweater (17-19:1) pass. Wall brightness changes by less than 4% over the clip.
10. **Flat, dense voice from heavy limiting (a recording-stage problem)** (0.11-7.43 s). Crest factor is 10.4 dB, peak-to-loudness ratio 7.8 dB (natural speech is about 18) and loudness range 0.6 LU. The voice sounds pushed and tiring, and the limiting cannot be undone.
11. **Crushed blacks, a baked-in teal/orange grade and slightly pink skin: the image is fragile** (Whole clip). 6.5-7.9% of pixels are at 5 or below in all three channels, and the sweater has no texture. Red is clipped in the wall and blue in the lamp. Her face's skin hue is 108-116 degrees against 121-123 on her neck. The wall has banding that is invisible at normal viewing. Highlights are not clipped.
12. **Hands are soft and smear on the two fast gestures** (1.80-1.95 s and 4.47-4.60 s). Focus is correctly on her face. Her hands are in front of the focus point (sharpness 4.5-6.7 against 43-64 on the eyes) and smear during the fast moves. Her eyes are closed at 1.87 s and squinting at 4.54 s.
13. **[CRITIC, not audited] Rights and the speaker's consent** (n/a). No auditor checked who owns this footage or whether the speaker agreed to a re-edit. The clip looks cut from a longer video, since it opens on 'Lekin'. Adding graphics to someone else's video does not make it the user's.
14. **[CRITIC, not audited] The fragment problem is patched, not solved** (0.11-0.44 s). 'ye drug' refers to context the clip does not have. The hook turns that into a quiz, but viewers may still wonder why Xylazine matters, and text cannot answer that without inventing claims.
15. **[CRITIC, not audited] Accessibility beyond contrast** (Whole clip). Only contrast was measured. Burned-in captions alone don't help viewers who rely on caption files, and the on-screen text leaves out 'Lekin', 'ek' and the 'hai' at the end. No limits were set for motion or flashing.
16. **[CRITIC, not audited] Sensitive topic: platform distribution and accuracy** (2.545 s (name), 3.99-5.09 s (glosses)). The auditors wrote content guardrails, but nobody checked the platform side: drug-related posts can get limited reach or an age gate if they show paraphernalia or use. Nobody who knows the full video has confirmed the drug name either. It was identified from the sounds alone, since Whisper never spelled it. 'UNCONSCIOUS' is a literal translation of 'behosh'.
17. **[CRITIC, not audited] Platform safe zones were inferred from the picture, not the app UI** (Whole clip). The auditors marked free areas by what is in the frame. The real limit is what the Reels, TikTok and Shorts interfaces draw over the video: tabs at the top, the caption, username and music line at the bottom, and the button column on the right.
18. **[CRITIC, not audited] Loudness was simulated, not measured on a real render** (Whole render). Every loudness figure comes from an offline numpy mix. Nobody has measured what the HyperFrames render and its AAC encode actually produce, or checked it against the platforms' own normalisation (about -14 LUFS, which only turns loud files down).
19. **[CRITIC, not audited] The end frame, freeze seam and loop were never checked in an actual render** (7.40-8.20 s and frame 0). Removing frame 223 depends on how the renderer rounds the clip's end. A PNG freeze frame can shift colour at the seam (BT.601 vs BT.709 colour matrix, or TV vs PC range). Nobody has looked at the loop seam or the cover frame.

### Edit brief (binding plan for the build)

```text
EDIT BRIEF: Xylazine explainer (Hinglish talking head, 9:16, about 8 s)

0. WHERE, WHAT, SOURCE OF TRUTH
- Build in /home/user/hyperframe/videos/xylazine-explainer/ (meta id "xylazine-explainer"). Do NOT touch the repo-root index.html, transcript.json or compositions/; they belong to the earlier "reinvent yourself" project.
- Skills: /hyperframes, then /talking-head-recut (designed overlays over untouched footage). Load /hyperframes-core, /hyperframes-keyframes (camera), /hyperframes-animation (typewriter, stamp), /hyperframes-audio (effect chains and volume lanes) and /media-use (SFX files, freeze segment). Skip the /media-use media treatments: the footage's look is not changed.
- Picture and voice: assets/speaker.mp4 (1620x2880, 30 fps, 224 frames, SDR BT.709; audio sample-aligned to the source). assets/source.mp4 (4K, 29.97 fps) is for reference only.
- Load GSAP from assets/vendor/gsap.min.js. Load Montserrat 700/800/900 from assets/fonts with explicit @font-face rules, and confirm in a snapshot that Montserrat is rendering rather than a fallback.
- Timing: replace the project's draft transcript.json with /tmp/claude-0/-home-user-hyperframe/3c6f00ae-cf89-5d82-9bbb-3ba15ee407ca/scratchpad/v3/agents/transcript/corrected_words.json (27 words, ids w0-w26, including "ek"). The draft runs 60-260 ms late and drops "ek". These corrected times override the script auditor's anchors.
- Corrected words (start-end, s): Lekin .110-.355 · ye .355-.435 · drug .435-.710 · actually .710-1.105 · karta 1.105-1.445 · kya 1.445-1.625 · hai? 1.625-1.740 · [pause 1.740-1.935] · Iska 1.935-2.145 · naam 2.145-2.420 · hai 2.420-2.545 · Xylazine 2.545-3.190 · jo 3.190-3.360 · animals 3.360-3.860 · ko 3.860-3.990 · behosh 3.990-4.540 · ya 4.540-4.645 · shaant 4.645-5.085 · karne 5.085-5.330 · ke 5.330-5.395 · liye 5.395-5.505 · di 5.505-5.655 · jaane 5.655-5.920 · wali 5.920-6.200 · ek 6.200-6.385 · veterinary 6.385-6.985 · drug 6.985-7.270 · hai. 7.270-7.440
- Structure: index.html (root, camera, video clips, audio) + compositions/plate.html (the one graphics plate, 0-8.2 s; its contents change state beat by beat) + compositions/captions.html (one caption track, 0-8.2 s).

1. CANVAS AND CLIPS
- Root: data-width 1080, data-height 1920, data-fps 30, data-duration 8.2 (246 frames). Render with --fps 30 --quality delivery (CRF 16 or lower, which keeps the wall gradient from banding after re-encode).
- #cam: a full-frame 1080x1920 wrapper with transform-origin 565px 870px. It carries every camera move. Inside it:
  a) <video id="speaker" class="clip" src="assets/speaker.mp4" data-start="0" data-duration="7.42" data-media-start="0" data-track-index="0" data-has-audio="true" playsinline>, at 1080x1920 with object-fit: cover (an exact 1/1.5 scale).
  b) <video id="hold" class="clip" src="assets/hold-f222.mp4" data-start="7.42" data-duration="0.78" data-track-index="1" muted playsinline>, same size and fit.
- Make the hold as a video segment, not a PNG. It then decodes the same way as the speaker clip, so colour can't jump at the seam. For example: ffmpeg -i assets/speaker.mp4 -vf "select=eq(n\,222),setpts=N/30/TB,tpad=stop_mode=clone:stop_duration=1" -r 30 -an -c:v libx264 -crf 12 -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv assets/hold-f222.mp4. Confirm it shows frame 222: mouth closed, eyes open, hand at chest level (x 460-750, y 1130-1300).
- Proxy frame 223 (7.4333-7.4667 s) is a one-frame cut to a different take and must never render. data-duration 7.42 ends the speaker clip after frame 222 (t = 7.400).
- If the user declines the hold: set the root data-duration to 7.42, delete #hold and sfx-end-button, and leave everything else unchanged.

2. LAYOUT (canvas px at 1.0x camera)
- GRAPHICS PLATE (the only plate): x 70-1010, y 230-570. Content box with 36 px padding: x 106-974, y 266-534. Rows: A y 266-330, B y 344-454, C y 468-534. Never go above y 220 (platform header) or below y 575. Her head top is at y 628-648 at 1.0x and about 589 at the 1.16x maximum zoom, so the shadow must stay tight: 0 8px 24px.
- CAPTION BAND: centred on x 540 inside x 120-940; one line within y 1400-1490. Two lines are allowed only for chunk C4 (y 1380-1510; her hands stay clear of it from 5.0 to 6.3 s). It sits over the black sweater, where white text is about 17:1.
- NO TEXT: face x 405-700, y 700-1050 (at 1.15x: x 380-725, y 670-1100); gesture zone x 180-950, y 960-1380; light glint x 830-870, y 945-1000; platform UI y < 220, y > 1520, x > 940 for y 850-1700, x < 60.
- Hands cross the caption band at 1.80-1.95 s and 4.47-4.65 s, and fingertips reach y 1445 near x 660-800 at 2.4-3.0 s. Captions therefore get text-shadow 0 0 2px rgba(0,0,0,.9), 0 2px 12px rgba(0,0,0,.6).
- Not used by default: left of her head, x 40-280, y 620-930 (over the lamp, light wall), and right of her head, x 790-940, y 600-900 (teal wall, 2.5-3.3:1).

3. LOOK (sober and clinical)
- Plate: #0C1715 at 88% opacity, radius 28, hairline border rgba(255,255,255,.08). White text on it is about 13:1 even over the cream hotspot. Nothing else covers the wall: no scrims, gradients, blur or vignette.
- Colours: text #F7F5F0; secondary text #F7F5F0 at 62%; accent amber #F2A33A (taken from the lamp); chips #F7F5F0 fill with #111 text; stamp #F2A33A fill with #111 text. No red, nothing flashing.
- Type: Montserrat 900 for the name and the stamp, 800 for the headline, chips and captions. ALL CAPS only on key-term graphics.
- Icons: an inline SVG paw, and a vet badge (the same paw in a rounded shield with a small plus). No other icons.
- Motion: entrances 0.18-0.30 s power3.out; exits 0.15-0.20 s power2.in. The only overshoot is the stamp (back.out(1.4)); no bounce, elastic or shake. Use one paused root timeline, window.__timelines["xylazine-explainer"]; scene timelines added to it are not paused. Repeats must be finite (the caret blink). No Math.random, Date.now or network calls.

4. ON-SCREEN LANGUAGE (default: mixed)
- Captions are verbatim Roman Hinglish in sentence case. Fixed spellings: ye, drug, actually, karta, kya, hai, Iska, naam, jo, animals, ko, behosh, ya, shaant, karne, ke, liye, di, jaane, wali, ek, veterinary.
- Key-term graphics are English ALL CAPS, using only her words or a direct translation: XYLAZINE, ANIMALS, UNCONSCIOUS / CALM (for "behosh ya shaant"), VETERINARY DRUG.
- "Lekin" is left off the screen only; the audio is untouched. No pronunciation chip: she says "ZY-luh-zine", the dictionary has "-zeen", and a chip would contradict her. No Devanagari: no Devanagari font is installed.

5. CAPTION TRACK (one track)
- Montserrat 800, 60 px, letter-spacing 0. Words are #F7F5F0 at 78% opacity. The active word goes to 100% and scale 1.05 (inline-block, origin bottom centre) from its start time until the next word starts. Key terms are always amber #F2A33A and also get the active treatment: animals, behosh, shaant. Xylazine and veterinary drug appear as graphics, not captions.
- Swaps between consecutive chunks are hard cuts. A chunk appearing after an empty band fades in and rises 12 px over 0.12 s; exits take 0.10 s.
- Q: shown in the plate, not the band. "Ye drug actually karta kya hai?" 0.000-1.800. Amber highlight times: ye .355, drug .435, actually .710, karta 1.105, kya 1.445, hai? 1.625.
- C1 "Iska naam hai" 1.900-2.545 (Iska 1.935, naam 2.145, hai 2.420).
- 2.545-3.160: no caption; the name graphic carries it.
- C2 "jo animals ko" 3.160-3.990 (jo 3.190, animals 3.360, ko 3.860).
- C3 "behosh ya shaant" 3.990-5.085 (behosh 3.990, ya 4.540, shaant 4.645).
- C4 "karne ke liye / di jaane wali" (2 lines) 5.085-6.300 (karne 5.085, ke 5.330, liye 5.395, di 5.505, jaane 5.655, wali 5.920).
- 6.300 to the end: no caption; the VETERINARY DRUG stamp carries "ek veterinary drug hai".
- Also write captions.srt with the full verbatim text, including Lekin, Xylazine and "ek veterinary drug hai", for upload alongside the render.

6. BEATS (composition seconds; all graphics are in the plate)
B0 Hook, 0.000-1.800
- Frame 0 (the cover) already shows the plate fully readable. Rows A+B: headline "Ye drug actually / karta kya hai?" (70 px, 800, 2 lines). Row C: the name blank, 8 amber slots (6 px bars about 64 px wide, 14 px gaps) with a caret blinking on a 0.5 s period.
- 0.00-0.25: the plate settles from y +24 to 0 and scale 1.03 to 1.00 (power3.out). Opacity is 1 from frame 0; no fade-up.
- Headline words turn amber at the Q times. From 1.445 to 1.80, "kya hai?" pulses 1 to 1.06 to 1 (sine.inOut).
- 1.733: the 8 slots flash white, then amber, and nudge up 6 px over 0.15 s (pop SFX).
B1 Setup, 1.800-2.545
- 1.80-2.10 (power3.inOut): the headline shrinks to one line in row A (38 px, 60% opacity), and the slots move to row B and widen to about 84 px (8 px gaps). The caret keeps blinking.
- Camera from 1.93 to 2.545: 1.00 to 1.03 (sine.in). Caption C1.
B2 Name, 2.545-3.190 (the biggest hit)
- Letters type into the slots in Montserrat 900, about 124 px, white; the word must fit within 760 px. Times: X 2.545, Y 2.615, L 2.685, A 2.755, Z 2.825, I 2.895, N 2.965, E 3.035. Each letter rises from y +18 at opacity 0 over 0.08 s (power2.out) while its slot bar shrinks to nothing. Letters appear in fixed order with no scramble.
- 3.035-3.195: a 6 px amber underline draws left to right under the word.
- Camera 2.545-2.80: 1.03 to 1.15 (expo.out). The sub-bass hit lands at 2.56. No caption.
B3 What it does, 3.190-5.085
- 3.19-3.40: the headline fades out. XYLAZINE docks into row A (scale about 0.52, underline kept) with power3.inOut over 0.3 s, and stays there to the end.
- 3.37, row B: the paw (64 px) scales 0.6 to 1 (back.out(1.2), 0.2 s) and "ANIMALS" (64 px, 800) wipes in from the left (clip-path, 0.2 s). Pop SFX.
- 3.98, row C: a "UNCONSCIOUS" pill chip (44 px) slides from x -20 to 0 over 0.18 s. Key-press tick.
- 4.60, row C: "or" (36 px, 62% white) and a "CALM" chip slide in the same way, and UNCONSCIOUS drops to 85%. Key-press tick. The "calm" treatment is one slow breath on the CALM chip (1 to 1.02 to 1 over 0.8 s); nothing comic.
- Camera from 2.80 to 5.10 drifts 1.15 to 1.16 (linear).
B4 Rest, 5.085-6.320
- No new graphic and no SFX. At 5.20, rows B and C settle to 85% opacity. Camera 5.10-6.15: 1.16 to 1.06 (sine.inOut). Caption C4.
B5 Category and recap, 6.320-7.420
- 6.32, row B: the paw gains its shield and plus and becomes the vet badge (0.15 s crossfade). "ANIMALS" is replaced by the stamp "VETERINARY DRUG" (amber box, #111 text, 56 px 900, letter-spacing .02em), which lands from scale 1.15 to 1.00 (back.out(1.4), 0.22 s). The plate nudges from y +4 to 0 over 2 frames. Click SFX.
- Rows B and C return to 100%. The recap reads XYLAZINE / [badge] VETERINARY DRUG / UNCONSCIOUS or CALM, all her own words, and stays readable from 6.32 to 8.00 (1.68 s).
- Camera 6.32-6.67: 1.06 to 1.12 (power3.out), then from 6.67 to 7.42 a drift to 1.13. The voice fades from 7.37 to 7.42.
B6 End hold, 7.420-8.200 (default ON)
- #hold shows frame 222 under the same camera. Camera 7.42-8.20: 1.13 to 1.00 (sine.inOut), so the loop seam matches frame 0's framing.
- 8.00-8.17: the plate's text fades out while the plate moves back to its frame-0 transform (y +24, scale 1.03). The auto-loop then restarts on the same plate with the headline. Sub-bass end hit at about 7.47.

7. CAMERA (scale on #cam, origin 565px 870px; no translate or rotate)
0-1.93: 1.00 · 1.93-2.545: to 1.03, sine.in · 2.545-2.80: to 1.15, expo.out · 2.80-5.10: to 1.16, linear · 5.10-6.15: to 1.06, sine.inOut · 6.32-6.67: to 1.12, power3.out · 6.67-7.42: to 1.13, linear · 7.42-8.20: to 1.00, sine.inOut.
The maximum of 1.16 is still oversampled 1.29:1 on the proxy, so the picture stays sharp. Never punch in on the hands, and never land a move on 1.87 s or 4.54 s (eyes closed or squinting).

8. SFX
- Copy from /home/user/hyperframe/.claude/skills/media-use/audio/assets/sfx/ into assets/sfx/: whoosh.mp3, pop.mp3, impact-bass-1.mp3, key-press.mp3, click.mp3 and CREDITS.md (Pixabay Content License).
- Every cue is an <audio data-audio-group="sfx" class="clip"> under <hf-audio-group id="sfx" data-label="SFX">. The group's data-fx-chain is one limiter, {"type":"limiter","id":"g1","label":"SFX ceiling","params":{"limit":-1,"attack":5,"release":50,"level_out":0}}. It is a safety only: SFX-only peaks simulate at -3.6 dBTP.
- Level rule: a cue with a volume lane carries its level inside the lane (absolute values) and has no data-volume. This is the pattern videos/rockwood-method shipped with. A cue without a lane uses data-volume. Never use both on one clip. Write the JSON attributes double-quoted with &quot;.
- data-start is the moment minus the file's hit offset. Fields per cue: id | file | data-start | data-media-start | data-duration | level | chain/lane | hit | synced to:
  sfx-whoosh-in | whoosh.mp3 | 0.000 | 0.10 | 0.36 | -13 dB | lane 0.224@0, 0.224@0.31, 0@0.36 | swell peaks 0.05-0.06; must not peak later, because "Lekin" starts at 0.11 | plate settle
  sfx-pop-question | pop.mp3 | 1.615 | 0 | 0.35 | data-volume 0.398 (-8 dB) | none | 1.733, inside the only pause | slot flash
  sfx-sub-name | impact-bass-1.mp3 | 2.5015 | 0 | 0.70 | peak -18 dB | chain {"type":"saturate","id":"n1","label":"Phone-speaker bite","params":{"type":"tanh","threshold":-12,"output":0,"oversample":4}}; lane 0.126@0, 0.126@0.11, 0.0464@0.26, 0.0171@0.41, 0.0063@0.56, 0@0.70 | 2.56 | X lands + punch-in
  sfx-pop-animals | pop.mp3 | 3.252 | 0 | 0.35 | data-volume 0.316 (-10 dB) | none | 3.370, in the gap 3.31-3.41 | paw + ANIMALS
  sfx-tick-behosh | key-press.mp3 | 3.906 | 0 | 0.20 | data-volume 1.259 (+2 dB) | none | 3.980 | UNCONSCIOUS chip
  sfx-tick-shaant | key-press.mp3 | 4.526 | 0 | 0.20 | data-volume 1.259 (+2 dB) | none | 4.600; never later, or it masks the "sh" of shaant | CALM chip
  sfx-click-vet | click.mp3 | 6.270 | 0 | 0.105 | -3 dB | lane 0.708@0, 0.708@0.095, 0@0.105 (keeps only the first transient) | 6.321, in the k closure of "ek" | stamp
  sfx-end-button | impact-bass-1.mp3 | 7.415 | 0 | 0.75 | peak -18 dB | same saturate chain; lane 0.126@0, 0.126@0.10, 0.0464@0.28, 0.0171@0.46, 0.0063@0.64, 0@0.75 | about 7.47, after "hai." | hold; only when the hold is on
- Simulated with these values: mix -14.2 LUFS / -2.3 dBTP; the least audible word is "ya" at 0.957.
- Off by default; the user can opt in, and exact parameters are in the audio auditor's map: riser.mp3 building into the name, glitch-3.mp3 as a decode texture, impact-bass-2.mp3 as a low "sedation" sink.
- Never use: sparkle, chime, notification, ping, error, glitch-1, glitch-2, typing, whoosh-cinematic; per-letter typing ticks (they would sit on the /z/ sounds); syringe, pill, heartbeat, siren or horror sounds.

9. LOUDNESS
- Source voice: -7.6 LUFS, +0.2 dBTP, already brickwall-limited (loudness range 0.6 LU).
- On the speaker <video>, set no data-volume and add:
  data-fx-chain {"version":1,"nodes":[{"type":"gain","id":"n1","label":"Loudness -7.6 to -14 LUFS","params":{"gain":-6.4}}]}. This equals a volume of 0.479 and puts the voice alone at -14.0 LUFS / -6.2 dBTP.
  data-automation {"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":1},{"t":7.37,"v":1},{"t":7.42,"v":0}]}]}, a 50 ms tail fade before the clip ends.
- Put no compressor, EQ, de-esser, gate or limiter on the voice. It is already limited; a -1 dB ceiling would never act on -6.2 dBTP peaks, and it can't catch the sum of voice and SFX anyway. No music bed. If the user insists on one, keep it at least 24 LU under the voice with a voiceover carve.
- Pass/fail on the rendered MP4: ffmpeg -i <render> -af ebur128=peak=true -f null - must give -14 +/-1 LUFS integrated and a true peak at or below -1.0 dBTP. If the integrated level is off, move n1 and every SFX level by the same number of dB. If the true peak is too high, lower the cue playing at that moment; don't limit the voice.

10. ENDING
- The footage ends at 7.42 (frames 0-222), so frame 223 never renders. The voice fades 7.37-7.42; the vowel of "hai." stays intact.
- A 0.78 s freeze of frame 222 runs to 8.20 under the recap. Add no new text, call to action, handle, "Part 2" or "follow". The loop seam is handled as described in B6.

11. GUARDRAILS
- Claims are limited to: the name, "animals", "unconscious / calm" (her "behosh ya shaant"), "veterinary drug" and her question. Nothing about human use or effects, "not for humans", street use, "tranq" or "zombie drug", fentanyl, wounds, overdoses, antidotes or naloxone, dose, route, sources, prices, places or statistics. No "only for animals" or "sirf animals".
- No pills, capsules, syringes, needles, vials, powder, smoke, slumped figures or pill/syringe emoji. No red alerts, hazard tape, BREAKING or SHOCKING labels, censorship bars or "classified" styling. No comic knocked-out stars or dizzy spirals. Nothing flashes more than 3 times a second.
- The footage pixels stay untouched: no grade, contrast, saturation, LUT, sharpening, blur, vignette or scrim. The blacks are crushed and channels clipped, so changes would posterize, and the wall would band. Don't trim "Lekin". No speed changes.
- Text goes only in the plate or the caption band: never over the face or the gesture zone, and no dark graphics over the sweater.
- Times come only from the corrected word list. Mid-frequency SFX (whoosh, pop, click) only at the listed gap and closure times.
- Minimum text sizes: captions 60 px, chips 44 px, smallest text ("or") 36 px.

12. QA BEFORE DELIVERY
- npx hyperframes check passes on the project directory, with all contrast checks passing.
- Snapshots at 0.000 (cover), 1.733, 2.60, 3.10, 3.40, 4.00, 4.62, 5.60, 6.35, 7.40, 7.433, 8.00 and 8.167. Check that no text sits over the face or hands, the plate clears her hair at 1.16x, and the font is Montserrat.
- On the render, measure the frame difference (luma mean absolute difference at 270x480). From 7.400 to 7.433 it must be under 1.5, meaning no flash and no colour jump into the hold, and there must be no spike above 6 anywhere.
- Loudness as in section 9. Listen at 0.11 s ("Lekin"), 2.56 s ("Xylazine") and 4.60-4.70 s ("shaant") for any word buried under an SFX.
- Play at 0.5x and check that every caption highlight lands within one frame of its word. Deliver the MP4 and captions.srt.
```

### Open decisions (defaults in use)

- End hold. Default: YES, a 0.78 s freeze of the last clean frame (frame 222) under the recap, so the video runs 8.2 s. If no: the video ends at 7.42 s, the recap is readable for only about 1.1 s, and the end sound effect is dropped.
- On-screen language. Default: mixed. Captions are word-for-word Roman Hinglish; key-term graphics are English ALL CAPS (XYLAZINE, ANIMALS, UNCONSCIOUS / CALM, VETERINARY DRUG); 'Lekin' is left off the screen. Alternatives: all Roman Hinglish; English subtitles; or Devanagari, which first needs a Devanagari font added to the project.
- Ownership and consent. Default: we assume you own this clip or have the speaker's permission to re-edit and post it; the edit adds nothing that identifies her. Please confirm before publishing.
- Name, handle, call to action, 'educational' tag or end-card text. Default: none, so nothing is invented. Send a handle or credential line if you want one added to the end hold.
- Standalone short or part of a longer video. Default: a standalone short, opening on her question at frame 0. The clip starts mid-thought ('Lekin ye drug...'), so if the full recording exists, including the sentence before it is the better fix, and the hook and end hold would then be dropped.
- Spelling of the drug name. Default: 'Xylazine'. It was identified from the audio and the context, and the transcription never spelled it. Please confirm.
- Pronunciation guide under the name. Default: OFF. She says 'ZY-luh-zine' and the dictionary says 'ZY-luh-zeen', so a guide would contradict her. If ON, the dictionary form appears under XYLAZINE.
- Sound-effect intensity. Default: a restrained set of 7 cues (soft whoosh in, two pops, a sub-bass hit on the name, two soft ticks, a stamp click) plus one end hit. Optional extras, off by default: a riser leading into the name, a glitch texture on the name reveal, and a low sub-bass 'sedation' tone under 'behosh ya shaant'.
