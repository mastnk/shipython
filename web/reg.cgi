#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb; cgitb.enable()

import os
import cgi
import datetime
import json
import fcntl
import hashlib

import openpyxl

import lock

form = cgi.FieldStorage()

try:
    ID = form.getvalue('ID')
except:
    ID = None

try:
    file = form.getvalue('file')
except:
    file = None

try:
    code = form.getvalue('code')
except:
    code = None

try:
    count = int(form.getvalue('count'))
except:
    count = None

try:
    accesskey = form.getvalue('accesskey')
    accesskey = hashlib.md5(accesskey.encode('utf8')).hexdigest().upper()
except:
    accesskey = None

try:
    ip = os.environ['REMOTE_ADDR']
except:
    ip = '0.0.0.0'

timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

res = {
'ID': ID,
'file': file,
'code': code,
'count': count,
'timestamp': timestamp,
'ip': ip,
}

'''
res = {
'ID': '0123',
'file': 'testA00.py',
'code': '292E',
'count': 89,
'timestamp': timestamp,
'ip': ip,
}
'''

def func( args ):
    res = args['res']
    accesskey = args['accesskey']

    try:
        wb = openpyxl.load_workbook('check.xlsx')
        ws_code = wb['code']
        ws_check = wb['check']
        ws_count = wb['count']
    except:
        res['res'] = 'Can not find correct check.xlsx.'
        return res

    IDs_code = [ c.value for c in ws_code['A'] ][1:]
    IDs_check = [ c.value for c in ws_check['A'] ][1:]
    IDs_count = [ c.value for c in ws_count['A'] ][1:]

    files_code = [ c.value for c in ws_code['1'] ][1:]
    files_check = [ c.value for c in ws_code['1'] ][1:]
    files_count = [ c.value for c in ws_count['1'] ][1:]

    if( IDs_code != IDs_check or IDs_code != IDs_count or \
        files_code != files_check or files_code != files_count ):
        res['res'] = 'Can not find correct check.xlsx.'
        return res

    try:
        row = IDs_code.index( res['ID'] ) + 2
    except:
        res['res'] = 'Can not find ID: ' + str(res['ID'])
        return res

    try:
        col = files_code.index( res['file'] ) + 2
    except:
        res['res'] = 'Can not find file: ' + str(res['file'])
        return res

    try:
        code = ws_code.cell(row=row, column=col).value
        code = code.split(',')
    except:
        res['res'] = 'Can not find code.'
        return res

    if( code[0] != res['code'] ):
        res['res'] = 'The code does not match: ' + str(res['code'])
        return res

    if( code[1] != accesskey ):
        res['res'] = 'The access key does not match.'
        return res

    d = ws_count.cell(row=row, column=col).value
    if( d is not None and d < count ):
        res['res'] = 'Already registered: ' + str(ws_check.cell(row=row, column=col).value)
        return res

    try:
        c = ws_check.cell(row=row, column=col)
        c.value = '{},{},{}'.format( res['timestamp'], res['ip'], res['code'] )
        c.number_format = openpyxl.styles.numbers.FORMAT_TEXT
        ws_count.cell(row=row, column=col).value = res['count']
        wb.save('check.xlsx')
    except:
        res['res'] = 'Can not write check.xlsx'
        return res

    res['res'] = 'OK'
    return res

res = lock.process( 'LOCK', func, res=res, accesskey=accesskey )

print("Content-Type: application/json; charset=UTF-8")
print("")
print(json.dumps(res))

