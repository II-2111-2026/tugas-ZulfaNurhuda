#!/bin/bash
set -euo pipefail

python -m pip install -U pip
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

quarto render