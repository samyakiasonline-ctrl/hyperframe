#!/bin/bash
# Prepares a Claude Code cloud session for HyperFrames: warms the pinned CLI
# and downloads Chrome Headless Shell, which local rendering requires.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

# Version pinned in package.json scripts, so renders stay reproducible.
HF_VERSION=$(grep -oE 'hyperframes@[0-9]+\.[0-9]+\.[0-9]+' package.json | head -1)

export HYPERFRAMES_SKIP_SKILLS=1
npx --yes "$HF_VERSION" --version >/dev/null
npx --yes "$HF_VERSION" browser ensure >/dev/null
