#!/usr/bin/env sh

cp id2xls.py shipython
cd shipython

python id2xls.py --id ../IDs.txt --xls ../check.xlsx

rm id2xls.py
