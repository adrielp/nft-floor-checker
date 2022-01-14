#!/usr/bin/env zsh

# Run Python venv, activate the environment, then run a pip install
# of the developer requirements.txt

python3 -m venv venv \
    && source venv/bin/activate \
    && pip install -r requirements.txt
