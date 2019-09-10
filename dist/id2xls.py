#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Library
import os
import sys
import glob
import importlib
import argparse

# Python Package
from openpyxl import Workbook

# Local Package
from TEST.test import test

parser = argparse.ArgumentParser()
parser.add_argument('--id', '-i', default='IDs.txt')
parser.add_argument('--xls', '-x', default='check.xlsx')
parser.add_argument('--dev', action='store_true', default=False)
args = parser.parse_args()


wb = Workbook()
ws = wb.active
ws.title = 'code'
wb.create_sheet('check')

ws_code = wb['code']
ws_check = wb['check']

with open(args.id, 'r') as fin:
    IDs = [ line.strip() for line in fin ]
IDs.sort()

for row, ID in enumerate(IDs, start=2):
    ws_code.cell( row=row, column=1 ).value = ID
    ws_check.cell( row=row, column=1 ).value = ID


files = glob.glob('TEST/test?*.py')
files = [ os.path.basename( file ) for file in files ]
files.sort()

for col, file in enumerate(files, start=2):
    print( file )

    ws_code.cell( row=1, column=col ).value = file
    ws_check.cell( row=1, column=col ).value = file
    for row, ID in enumerate(IDs, start=2):
        try:
            ws_code.cell( row=row, column=col ).value = test( file, ID, '', args.dev, False )
        except:
            pass

wb.save( args.xls )

