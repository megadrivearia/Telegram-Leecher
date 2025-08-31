#!/usr/bin/env bash
set -e
echo "Installing system packages (ffmpeg, aria2, libmagic)..."
sudo apt-get update -y
sudo apt-get install -y ffmpeg aria2 libmagic1 zip unzip
echo "Upgrading pip and installing Python requirements..."
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
echo "Done."
