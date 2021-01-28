#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_random.py
@Author : alexander.here@gmail.com   
@Date   : 2020-07-10 16:55 CST(+0800)   
@Brief  : https://docs.python.org/zh-cn/3/library/random.html

'''

from __future__ import print_function
import random

print( 'random.random() generates 0 <= X < 1.0:')
print( [ random.random() for i in range( 8)])

print( '\nrandom.uniform( A, B) generates floats A <= X <= B:')
print( [ random.uniform( -5, 5) for i in range( 5)])
print( [ random.uniform( 5, -5) for i in range( 5)])

print( '\nrandom.choice():') # use choices( datas, weights) for weighting
print( random.choice( 'hello'), 'from', "'hello'")
print( random.choice( range( 10)), 'from', 'range( 10)')

print( '\nrandom.shuffle():') # scramble in-place:
l = list( range( 10))
random.shuffle( l)
print( l)
s = list( "python")
random.shuffle( s)
print( ''.join( s))

print( '\nrandom.sample() can be used as choice() or shuffle():')
print( random.sample( [ 1, 3, 5, 7], 2))        # choose 2 elements from container
print( random.sample( range( 10), 1)[ 0])       # as choice()
print( ''.join( random.sample( 'python', 6)))   # as shuffle()

# random.randrange( start, stop[, step]) works just like:
# random.choice( range( start, stop, step)) without actually creating range() object.

# random.randint( a, b) is equivalent to random.randrange( a, b+1)

# set seed:
print( "\nfixed seed:")
random.seed( 1)
print( [ random.random() for i in range( 3)])
random.seed( 1)
print( [ random.random() for i in range( 3)])

# End of 'use_random.py' 

