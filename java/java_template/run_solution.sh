#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Compile Solution.java to out/ and run it
"$SCRIPT_DIR"/build.sh
java -cp "$SCRIPT_DIR/out" Solution | cat


