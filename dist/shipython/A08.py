#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Rotate the list, where the right is positive direction.
#  n=2, [ 1, 2, 3, 4, 5 ] -> [ 4, 5, 1, 2, 3 ]
#

ID = '01234'


def func( li, n ): # li: list(int), n: int
    # edit here
    return li


###############################################################
# DO NOT EDIT BELOW
def sample( func ):
    print( "func( [1,2,3,4,5], 2 )\n => {} ([4,5,1,2,3,4])".format( func( [1,2,3,4,5], 2 ) ) )
    print( "func( [1,2,3,4,5], 0 )\n => {} ([1,2,3,4,5])".format( func( [1,2,3,4,5], 0 ) ) )
    print( "func( [1,2,3,4,5], -1 )\n => {} ([2,3,4,5,1])".format( func( [1,2,3,4,5], -1 ) ) )



###############################################################
if( __name__ == '__main__' ):
    sample( func )


#################
# created by
#    name: Masayuki Tanaka
# twitter: http://twitter.com/likesilkto
#  github: http://github.com/mastnk
#     url: http://www.ok.sc.e.titech.ac.jp/~mtanaka/
