#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : bool.py   
@Author : alexander.here@gmail.com   
@Date   : 2020-02-18 12:09   
@Brief  :  

'''

def my_exec( statement):
    print( ">>> " + statement)
    exec( statement) # use eval() for expressions

# Literals :
value = True
value = False

# Operators:
my_exec( 'print( not True)')
my_exec( 'print( False and True)')
my_exec( 'print( False or True)')
my_exec( 'print( not False and False)') # 'not' first

# Special Operators:
my_exec( 'print( 234 in { 123, 234, 345} )') # also works for 
my_exec( 'print( "234" not in { 123, 234, 345} )')

# 'x is y' is the same with 'id( x) == id( y)':
my_exec( 'print( "hello" is "hello")')
my_exec( 'print( 1 is not 2)')
l1 = [ 1, 2, 3]
l2 = l1
l1.append( 4)
my_exec( 'print( l1 is l2 )')
my_exec( 'print( ( 1, 2, 3) is ( 1, 2, 3) )')
my_exec( 'print( [ 1, 2, 3] is [ 1, 2, 3] )')


# End of 'bool.py' 

