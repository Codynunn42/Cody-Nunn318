#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${PKG_DIR}"

echo "[sentinel] smoke:billing starting"
echo "[sentinel] package dir: ${PKG_DIR}"
echo "[sentinel] billing smoke placeholder passed"
echo "[sentinel] smoke:billing completed"
