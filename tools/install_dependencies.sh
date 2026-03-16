#!/bin/bash
set -euo pipefail

python -m pip install --upgrade pip

if [ -f requirements.txt ] && [ -s requirements.txt ]; then
    for i in {1..3}; do
        pip install -r requirements.txt && break || sleep 5
    done
fi

mkdir -p ~/.cache/pip