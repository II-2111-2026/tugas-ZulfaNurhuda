#!/bin/bash
set -euo pipefail

python -m pip install -U pip
pip install -r requirements.txt

quarto render