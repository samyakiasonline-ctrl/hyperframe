# hyperframe

Video editing workspace built on [HyperFrames](https://github.com/heygen-com/hyperframes):
write a composition in HTML (footage, overlays, captions, animation), then render it to MP4.

## Requirements

Node.js 22+ and FFmpeg. The first render needs Chrome Headless Shell:

```bash
npx hyperframes browser ensure
```

(Claude Code cloud sessions run this automatically via `.claude/hooks/session-start.sh`.)

## Usage

```bash
npm run dev      # preview in the Studio with live reload
npm run check    # lint, runtime, layout, motion and contrast checks
npm run render   # render index.html to renders/<name>.mp4
```

To edit your own footage, drop it in `assets/` and reference it from `index.html`
(or a sub-composition in `compositions/`) as a `<video class="clip">` with
`data-start`, `data-duration` and, to trim, `data-media-start`.

## With Claude Code

The HyperFrames skills are vendored in `.claude/skills/`, so Claude Code picks them up in
this repo with no install. Start with a prompt such as:

> Using /hyperframes, add captions to assets/interview.mp4

> Using /hyperframes, recut assets/talk.mp4 with lower-thirds and a title card

Refresh the skills from upstream with `scripts/update-skills.sh`.
