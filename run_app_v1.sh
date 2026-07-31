#!/bin/bash

echo "[START] Web app web_v1"

cd apps/web_v1
export PYTHONPATH=../../math_core/src:$PYTHONPATH
export FLASK_APP=flask_app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=7850

echo "[END] Web app web_v1"
