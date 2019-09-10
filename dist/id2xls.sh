#!/usr/bin/env sh

cp id2xls.py shipython
cd shipython

python id2xls.py --id ../IDs.txt --xls ../check.xlsx ${1}
#python id2xls.py --id ../IDs.txt --xls ../check.xlsx --dev

rm id2xls.py
