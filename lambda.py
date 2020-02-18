#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : lambda.py   
@Author : zoujiachen@megvii.com   
@Date   : 2020-01-13 18:36   
@Brief  :  

'''

# SYNTAX:
# lambda [ARGS...] : one and only one expression, no statements

x = 123
f = lambda : x + 1
print( f())
# note that 'x' in lambda f is part of an expression, not a reference.
# meaning of it changes with the scope!

x = 321
g = lambda x, y : ( x * 2, y())
print( g( 3, f))


# End of 'lambda.py' 

