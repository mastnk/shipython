#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Replace four-character word starting with "F" or "f" by "***".
#

ID = '01234'


def func( str ): # str: string
    return str


###############################################################
# DO NOT EDIT BELOW
def sample( func ):
    print( "func( u'Where is fifth avenue?' )\n => {} (Where is fifth avenue?)".format( func( u'Where is fifth avenue?' ) ) )
    print( "func( u'One, two, three, four, five, six.' )\n => {} (One, two, three, ****, ****, six.)".format( func( u'One, two, three, four, five, six.' ) ) )
    print( "func( u'Fill in this application form.' )\n => {} (**** in this application ****.)".format( func( u'Fill in this application form.' ) ) )


###############################################################
if( __name__ == '__main__' ):
    sample( func )


#################
# created by
#    name: Masayuki Tanaka
# twitter: http://twitter.com/likesilkto
#  github: http://github.com/mastnk
#     url: http://www.ok.sc.e.titech.ac.jp/~mtanaka/
