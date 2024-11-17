#!/bin/bash
set -e  # Exit on any error

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Running script from: $BASE_DIR"

# Install Python dependencies
python3 -m pip install --upgrade pip requests

# Execute the Python script to generate the M3U playlist
cd "$BASE_DIR/scripts"
python3 main.py > "$BASE_DIR/youtube.m3u"

echo "Playlist generation complete."
