#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : function.py   
@Author : alexander.here@gmail.com   
@Date   : 2020-01-13 14:53   
@Brief  :  

'''

def foo( arg1, arg2, arg3 = 'default3', arg4 = 'default4'):
    print( "arg1: " + str( arg1))
    print( "arg2: " + str( arg2))
    print( "arg3: " + str( arg3))
    print( "arg4: " + str( arg4))
    print( "")

# functions can be referenced:
func = foo

func( 1, 'xyz', arg4 = '!!!')

# partial / bind function:
from functools import partial

# func( arg3 = 'default3', arg4 = 'default4') = foo( 123, 456, arg3, arg4):
func = partial( foo, 123, 456)
func( arg4 = 789)

# func( arg2, arg4 = 'default4') = foo( 987, arg2, 321, arg4):
func = partial( foo, 987, arg3 = 321)
func( 654)

# End of 'function.py' 

