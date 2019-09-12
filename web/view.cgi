#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb; cgitb.enable()


import os
import sys
import cgi

import openpyxl

import lock

def output_html( main, file = '' ):
    HTML = '''
<html>
 <head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
 <title> ShiPython </title>
 </head>
 <body>
 <center>

 <h1> ShiPython </h1>
 <form action="view.cgi" method="post">
 <table>
   <tr>
    <td align="right">ID: </td>
    <td align="left"><input type="text" name="ID" size="40"></td>
   </tr>
   <tr>
    <td align="right">code [{file}]: </td>
    <td align="left"><input type="code" name="code" size="40"></td>
   </tr>
  </table>
  <input type="submit">
  </form>

  <font size="2"><a href="https://github.com/mastnk/shipython">Powered by ShiPython</a></font>

 <hr />

{main}

 </center>
 </body>
</html>
'''.format(main=main, file=file)

    print("Content-Type: text/html; charset=UTF-8")
    print("")
    print(HTML)


form = cgi.FieldStorage()

try:
    ID = form.getvalue('ID')
except:
    ID = None

try:
    code = form.getvalue('code')
except:
    code = None

def load_workbook( args ):
    return openpyxl.load_workbook(args['filename'])

try:
#    wb = openpyxl.load_workbook('check.xlsx')
    wb = lock.process( 'LOCK', load_workbook, filename='check.xlsx' )
    ws = wb['check']
    wsc = wb['count']
    file0 = ws.cell( row=1, column=2 ).value
except:
    main = '<font color="red"> Error: Can not open check.xlsx </font>'
    output_html( main )
    sys.exit()

main = ''

if( ID is not None and code is not None ):
    IDs = [ c.value for c in ws['A'] ][1:]
    if( not ID in IDs ):
        main = '<font color="red"> Error: Can not find ID: {} </font>'.format( ID )
        output_html( main, file )
        sys.exit()

    row = IDs.index( ID ) + 2
    code0 = wb['code'].cell( row=row, column=2 ).value
    code0 = code0.split(',')
    if( code != code0[0] ):
        main = '<font color="red"> Error: Code does not match: {} </font>'.format( code )
        output_html( main, file0 )
        sys.exit()

    files = [ c.value for c in ws['1'] ][1:]

    main += '<h2>{}</h2>\n'.format(ID)
    main += '<table border="1" cellpadding="3" style="border-collapse: collapse">\n'
    main += '<tr><th>TestName</th><th>char count</th><th>ranking</th><th>time stamp</th><th>ip</th></tr>\n'
    for col, file in enumerate(files, start=2):

        c = wsc.cell( row=row, column=col ).value
        if( c is None ):
            c = ''
            r = ''
        else:
            try:
                cs = [ cc.value for cc in list(wsc.columns)[col-1] ][1:]
                cs = [ cc for cc in cs if cc is not None ]
                cs.sort()
                r = cs.index(c)+1
            except:
                r = ''

        v = ws.cell( row=row, column=col ).value
        if( v is None ):
            v = ['', '']
        else:
            try:
                v = v.split(',')[:2]
            except:
                v = ['', '']



        main += '<tr><td>{}</td><td align="center">{}</td><td align="center">{}</td><td>{}</td><td>{}</td></tr>\n'.format( file, c, r, v[0], v[1] )
    main += '</table>\n'

output_html( main, file0 )

