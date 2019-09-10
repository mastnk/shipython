#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Remove successive characters in the text.
#  'Hello!' -> 'Helo!'
#

ID = '01234'


def func( text ): # text: string
    # edit here
    return text


###############################################################
# DO NOT EDIT BELOW
def sample( func ):
    print( "func( u'Hello!' )\n => {} (u'Helo!')".format( func( u'Hello!' ) ) )
    print( "func( u'I get an egg.' )\n => {} (u'I get an eg.')".format( func( u'I get an eg.' ) ) )
    print( "func( u'My bedroom door was opened.' )\n => {} (u'My bedrom dor was opened.')".format( func( u'My bedroom door was opened.' ) ) )



###############################################################
if( __name__ == '__main__' ):
    sample( func )


#################
# created by
#    name: Masayuki Tanaka
# twitter: http://twitter.com/likesilkto
#  github: http://github.com/mastnk
#     url: http://www.ok.sc.e.titech.ac.jp/~mtanaka/
