#!/bin/zsh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR"/build.sh
java -cp "$SCRIPT_DIR"/out Judge


