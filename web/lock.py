#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fcntl

def process( lockfilename, func, **kargs ):
    ret = None
    with open(lockfilename) as fLock:
        fcntl.flock(fLock.fileno(), fcntl.LOCK_EX)
        try:
            ret = func(kargs)
        finally:
            fcntl.flock(fLock.fileno(), fcntl.LOCK_UN)
    return ret

