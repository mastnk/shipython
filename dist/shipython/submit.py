#!/usr/bin/env python
# -*- coding: utf-8 -*-

URL = ''





# Standard Library
import sys
import os
import re
import glob
import importlib
import platform
import warnings

# Local Package
from TEST.test import test
from TEST.util import PASSED, FAILED

def getName( ind ):
    try:
        name = sys.argv[ind]
    except:
        print( 'usage: python submit.py [--dev] ???.py ' )
        sys.exit()
    return name

VER = '3.6.0'
if( platform.python_version() < VER ):
    warnings.warn( '\nVersion of this python is ' + platform.python_version() + f'.\nVer. {VER} or later is recommended.', stacklevel=2 )

name = getName( 1 )
if( name == '--dev' ):
    name = getName( 2 )
    dev = True
else:
    dev = False

names = sorted(glob.glob( name ))

if( len( names ) == 0 ):
    print( 'Can not find file: ' + name )
    sys.exit()

elif( len( names ) == 1 ):
    name = re.sub( '\.py$', '', names[0] )
    n = importlib.import_module( name )
    test( 'test'+name+'.py', n.ID, URL, dev )

else:
    pf = [0] * 2
    for name in names:
        name = re.sub( '\.py$', '', name )
        n = importlib.import_module( name )
        code = test( 'test'+name+'.py', n.ID, URL, dev, False )
        msg = name+'.py '
        if( code is None ):
            msg += FAILED
            pf[1] += 1
        else:
            msg += PASSED + ' ' + code
            pf[0] += 1
        print( msg )

    print()
    print( PASSED + ': ' + str(pf[0]) )
    print( FAILED + ': ' + str(pf[1]) )

