#!/usr/bin/env bash

# get script dir
script_dir=$( cd `dirname ${BASH_SOURCE[0]}` >/dev/null 2>&1 ; pwd -P )

pushd $script_dir > /dev/null

# Node.js
echo "Node.js ..." 

source ~/.nvm/nvm.sh
nvm use

# Python
echo "Python ..."

# Do not install Python if in Anaconda environment or we are on Docker container
if [[ -z "$CONDA_DEFAULT_ENV" && ! -f /.dockerenv ]]
then
    # install Python 3.12.0 if not installed
    pyenv install 3.12.0 --skip-existing
    pyenv versions

    # use Python 3 from .python-version for local development
    eval "$(pyenv init -)"
fi

# create virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# upgrade pip
pip install --upgrade wheel
pip install --upgrade pip

# install packages
pip install -r requirements.txt
pip install -r requirements-dev.txt

popd > /dev/null
