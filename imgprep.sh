#!/bin/bash
WD=$(dirname -- $(readlink -f "$0"))
PYTHONPATH="$WD" python3 -m imgprep.main