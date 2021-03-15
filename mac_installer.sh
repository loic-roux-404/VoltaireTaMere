#!/usr/bin/env bash

brew install chromedriver
brew install --cask miniconda
conda create --name=$(basename "$PWD") python=3.7
conda activate $(basename "$PWD")
pip3 install -r requirements.txt

echo "[ Launch chromedriver. To kill processes (kill -9 <PID>) : ps -a | grep chromedriver | awk '{ print \$1 }']"
chromedriver >/dev/null &
python3 Napoleon.py
