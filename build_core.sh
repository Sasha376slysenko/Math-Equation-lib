#!/bin/bash

echo "[START] Compile math_core"

pip install -e ./math_core

echo "[END] Compile math_core"


echo "[STAT] Compile math_equation_levels"

cd math_core
python setup_levels.py build_ext --inplace

echo "[END] Compile math_equation_levels"
