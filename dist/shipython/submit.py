#!/usr/bin/env python
# -*- coding: utf-8 -*-

URL = ''

# Standard Library
import sys
import os
import re
import importlib

# Local Package
from TEST.test import test

def getName( ind ):
    try:
        name = sys.argv[ind]
    except:
        print( 'usage: python submit.py [--dev] ???.py ' )
        sys.exit()
    return name

name = getName( 1 )
if( name == '--dev' ):
    name = getName( 2 )
    dev = True
else:
    dev = False

if( not os.path.exists( name ) ):
    print( 'Can not find file: ' + name )
    sys.exit()

name = re.sub( '\.py$', '', name )
n = importlib.import_module( name )
test( 'test'+name+'.py', n.ID, URL, dev )
