#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : md5.py   
@Author : alexander.here@gmail.com
@Date   : 2020-03-02 11:54 CST(+0800)   
@Brief  :  

'''

# see https://docs.python.org/3/library/hashlib.html for more info.

import hashlib

# string digest:
md5 = hashlib.md5()
md5.update( 'hello,')
md5.update( ' world.')
print( md5.hexdigest())
# NOTE: if not sure, encode to utf-8 before update()

# file digest:
md5 = hashlib.md5()
with open( 'md5.py', 'r') as me:
    buf = me.read( 4096)
    while len( buf) > 0:
        md5.update( buf)
        buf = me.read( 4096)
print( md5.hexdigest())



# End of 'md5.py' 

