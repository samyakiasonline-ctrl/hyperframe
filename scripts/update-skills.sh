#!/bin/bash
# Re-vendors the published HyperFrames skills from heygen-com/hyperframes main
# into .claude/skills, replacing the copies there.
set -euo pipefail

cd "$(dirname "$0")/.."
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

git clone --quiet --depth 1 --filter=blob:none --sparse \
  https://github.com/heygen-com/hyperframes.git "$tmp/hyperframes"
git -C "$tmp/hyperframes" sparse-checkout set skills

mkdir -p .claude/skills
for dir in "$tmp"/hyperframes/skills/*/; do
  name=$(basename "$dir")
  rm -rf ".claude/skills/$name"
  cp -r "$dir" ".claude/skills/$name"
done

echo "Updated skills to heygen-com/hyperframes@$(git -C "$tmp/hyperframes" rev-parse --short HEAD)"
