#!/bin/zsh
# e: exit if any command fails
# u: exit if any variable is not set
# o: exit if any command returns a non-zero exit code
set -euo pipefail


SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_DIR="$SCRIPT_DIR/out"
mkdir -p "$OUT_DIR"

javac -d "$OUT_DIR" "$SCRIPT_DIR"/src/*.java
