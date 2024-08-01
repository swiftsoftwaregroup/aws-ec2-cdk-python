#!/usr/bin/env bash

# Node.js
# use correct Node version
source ~/.nvm/nvm.sh
nvm use

# Python
cd app

source .venv/bin/activate

pip install -r requirements.txt
pip install -r requirements-dev.txt
