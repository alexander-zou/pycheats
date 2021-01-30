#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : with.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-30 11:51 CST(+0800)   
@Brief  :  

'''

# Use 'with' with open():

if '__file__' in vars():
    with open( __file__, 'r') as file:
        print( file.readlines()[ 16].strip())

# Use 'with' with user-defined-classes:

class Foo:
    def __enter__( self):
        print( '__enter__() called.')
        return self
    def __exit__( self, *exc_info):
        print( '__exit__() called.')
    def bar( self):
        print( 'bar() called.')

with Foo() as foo:
    foo.bar()




# End of 'with.py' 

