#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : unpacking.py   
@Author : alexander.here@gmail.com   
@Date   : 2023-06-28 11:51    (+0800)   
@Brief  :  

'''

# BASIC USE: assign values from a iterable object into multiple variables:

( x, y, z) = range( 3)
print( x, y, z)

# brackets can be left out:
x, y, z = range( 3)

# also works with tuple and list:
x, y, z = 0, 1, 2
x, y, z = [ 0, 1, 2]

# to exchange values:
x, y, z = y, z, x
print( x, y, z)


# use star operation to unpack a list while unpacking:
x, *y, z = 1, 2, 3, 4
print( y) # y is [2, 3]

# expand / merge list:
print( [ 'head', *y, 'middle', *y, 'tail']) # output: ['head', 2, 3, 'middle', 2, 3, 'tail']

# fill function arguments:
def func( x, y, z):
    print( f'func: x={x}, y={y}, z={z}')
func( 1, *y) # output:  x=1, y=2, z=3
func( *y, 4) # output:  x=2, y=3, z=4

# unpack dictionary:
args = {
    'x' : 123,
    'y' : 456,
    'z' : 789,
}
func( **args)

# expand / merge dict:
print( { 'bla':'bla', **args, **dict( enumerate( y))})

# End of 'unpacking.py' 

