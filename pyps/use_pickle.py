#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : use_pickle.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-03-31 11:27 CST(+0800)   
@Brief  :  

'''

import pickle
from io import BytesIO

class MyData:
    def __init__( self, data):
        self.data = data
    def who_am_i( self):
        print( self, self.data)

obj = MyData( 456)
obj.who_am_i()

# Serialize:
file = BytesIO()
pickle.dump( obj, file)
print( 'serialized into %d bytes:' % ( len( file.getvalue())))
print( " ".join( "%02x" % byte for byte in bytes( file.getvalue())))

# Unserialize
print( 'unserialized:')
file.seek( 0)
new_obj = pickle.load( file)
new_obj.who_am_i()



# End of 'use_pickle.py' 

