#!/bin/bash
set -e  # Exit on error

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Running from: $BASE_DIR"

# Install dependencies
python3 -m pip install --upgrade pip requests

# Change directory to scripts and run Python script
cd "$BASE_DIR/scripts"
python3 main.py > "$BASE_DIR/youtube.m3u"

echo "Playlist generation complete."
