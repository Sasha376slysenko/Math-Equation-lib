#!/bin/bash

echo "[START] check length arrays struct C export eq"

cd math_core/src_c
gcc eq_4.c eq_5.c eq_6.c eq_7.c eq_8.c main.c -o check_length
./check_length

echo "[END] check length arrays struct C export eq"