#!/usr/bin/env python
# -*- coding: utf-8 -*-

KEY = ''
URL = ''


if( __name__ == '__main__' ):
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


    VER = '3.6.0'
    if( platform.python_version() < VER ):
        warnings.warn( '\nVersion of this python is ' + platform.python_version() + f'.\nVer. {VER} or later is recommended.', stacklevel=2 )

    try:
        name = sys.argv[1]
    except:
        print( 'usage: python submit.py python_file ' )
        sys.exit()

    names = sorted(glob.glob( name ))

    if( len( names ) == 0 ):
        print( 'Can not find file: ' + name )
        sys.exit()

    elif( len( names ) == 1 ):
        name = re.sub( '\.py$', '', names[0] )
        n = importlib.import_module( name )
        test( 'test'+name+'.py', n.ID, KEY, URL )

    else:
        pf = [0] * 2
        for name in names:
            name = re.sub( '\.py$', '', name )
            n = importlib.import_module( name )
            code, accesskey = test( 'test'+name+'.py', n.ID, KEY, URL, False )
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

