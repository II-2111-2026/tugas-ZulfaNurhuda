#!/bin/bash
set -euo pipefail

WEEK="$1"

EXTRA="$(find . -name '*_test.py' -not -path './__active_tests__/*' -print | head -n 1 || true)"
if [ -n "$EXTRA" ]; then
    echo "Error: Found unexpected test file: $EXTRA. Please do not add *_test.py files. Put your work in submissions/$WEEK/answers.py."
    exit 1
fi

rm -rf __active_tests__
mkdir -p __active_tests__

if [ ! -f "checkers/$WEEK/quiz_tests.py" ]; then
    echo "Error: Missing checkers/$WEEK/quiz_tests.py"
    exit 1
fi

cp "checkers/$WEEK/quiz_tests.py" "__active_tests__/quiz_test.py"