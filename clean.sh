#!/bin/bash

echo "[START] Clean compile"

find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name "*.so" -delete
find . -type d -name "*.pyc" -delete
rm -rf math_core/build

echo "[END] Clean compile"
