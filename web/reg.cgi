#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import cgitb; cgitb.enable()


import os
import cgi
import datetime
import json

import fcntl
import openpyxl


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
    ip = os.environ['REMOTE_ADDR']
except:
    ip = '0.0.0.0'

timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

res = {
'ID': ID,
'file': file,
'code': code,
'timestamp': timestamp,
'ip': ip,
}

'''
res = {
'ID': 'hoge',
'file': 'testA01.py',
'code': '7B8D',
'timestamp': timestamp,
'ip': ip,
}
'''

def func( res ):
    try:
        wb = openpyxl.load_workbook('check.xlsx')
        ws_code = wb['code']
        ws_check = wb['check']
    except:
        res['res'] = 'Can not find correct check.xlsx.'
        return res

    IDs_code = [ c.value for c in ws_code['A'] ][1:]
    IDs_check = [ c.value for c in ws_check['A'] ][1:]

    files_code = [ c.value for c in ws_code['1'] ][1:]
    files_check = [ c.value for c in ws_code['1'] ][1:]

    if( IDs_code != IDs_check or files_code != files_check ):
        res['res'] = 'Can not find correct check.xlsx.'
        return res

    try:
        row = IDs_code.index( res['ID'] ) + 1
    except:
        res['res'] = 'Can not find ID: ' + str(res['ID'])
        return res

    try:
        col = files_code.index( res['file'] ) + 1
    except:
        res['res'] = 'Can not find file: ' + str(res['file'])
        return res

    try:
        code = ws_code.cell(row=row, column=col).value
    except:
        res['res'] = 'Can not find code.'
        return res

    if( code != res['code'] ):
        res['res'] = 'The code does not match: ' + str(res['code'])
        return res

    d = ws_check.cell(row=row, column=col).value
    if( d is None ):
        flg = False
    else:
        try:
            c = d.split(',')[1]
            if( code == c ):
                flg = True
            else:
                flg = False
        except:
            flg = False

    if( flg ):
        res['res'] = 'Already registered: ' + str(ws_check.cell(row=row, column=col).value)
        return res

    try:
        ws_check.cell(row=row, column=col).value = '{} ({}),{}'.format( res['timestamp'], res['ip'], res['code'] )
        wb.save('check.xlsx')
    except:
        res['res'] = 'Can not write check.xlsx'
        return res

    res['res'] = 'OK'
    return res

with open('LOCK') as fLock:
    fcntl.flock(fLock.fileno(), fcntl.LOCK_EX)
    try:
        res = func(res)
    finally:
        fcntl.flock(fLock.fileno(), fcntl.LOCK_UN)

print("Content-Type: application/json; charset=UTF-8")
print("")
print(json.dumps(res))


'''
ID = '01234'
file = 'testA00.py'
code = 'AA30'
title, ext = os.path.splitext( file )
'''

res = {
'ID': ID,
'file': file,
'code': code,
}

'''
def pack( code, timestamp, ip ):
    return '"' + code + ',' + timestamp + ',' + ip + '"'

def unpack( data ):
    return data[1:-1].split(',')


def mkcol( c, new_col ):
    sql = 'PRAGMA TABLE_INFO(mt)'
    c.execute(sql)
    cols = c.fetchall()
    for col in cols:
        if( col[1] == new_col ):
            return

    sql = 'ALTER TABLE mt ADD COLUMN {} TEXT'.format(new_col)
    c.execute(sql)

def adddata( c, ID, col, data ):
    sql = 'SELECT id, {col} FROM mt WHERE id="{ID}"'.format( col=col, ID=ID )
    c.execute(sql)
    d = c.fetchall()

    if( d==[] ):
        sql = 'INSERT INTO mt (id, {col}) VALUES (?,?)'.format( col=col )
        par = ( ID, data )
        c.execute(sql, par)
        ret = data

    else:
        ret = d[0][1]

    return ret


def exportcsv( c ):
    filename = 'reg.csv'

    c.execute('SELECT * FROM mt')
    with open( filename, 'w' ) as fout:
        csv_out = csv.writer(fout)
        csv_out.writerow([d[0] for d in c.description])
        for result in c:
            csv_out.writerow(result)

if( ID is not None and title is not None and code is not None and code == util.getCode( ID, title ) ):
    conn = sqlite3.connect('reg.db')
    c = conn.cursor()

    sql = 'CREATE TABLE IF NOT EXISTS mt (id TEXT PRIMARY KEY)'
    c.execute(sql)

    mkcol( c, title )

    try:
        res['ip'] = os.environ['REMOTE_ADDR']
    except:
        res['ip'] = '0.0.0.0'

    data = pack( code, timestamp, res['ip'] )
    data = adddata( c, ID, title, data )
    code, timestamp, ip = unpack( data )
    res['timestamp'] = timestamp

    conn.commit()

    exportcsv( c )

    conn.close()

    res['ret'] = 'OK'

else:
    res['ret'] = 'NG'

try:
    os.chmod( 'reg.db', 0o666 )
except:
    pass

try:
    os.chmod( 'reg.csv', 0o666 )
except:
    pass

print("Content-Type: application/json; charset=UTF-8")
print("")
print(json.dumps(res))
'''
