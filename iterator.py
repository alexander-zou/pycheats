#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : iterator.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-30 14:09 CST(+0800)   
@Brief  :  

'''

from __future__ import print_function

# Basic use:
it = iter( [ 'A', 'B'])
print( next( it))
print( next( it))
try:
    print( next( it))
except StopIteration:
    print( 'StopIteration Raised.')

# User-define iterator:
class FibonacciSequence:
    class Iter:
        def __init__( self, size):
            self.size = self.count = size
            self.prev, self.curr = 0, 1

        def __next__( self):
            if self.count <= 0:
                raise StopIteration
            self.count -= 1
            self.prev, self.curr = self.curr, self.prev + self.curr
            return self.prev

        def next( self): # for Python2 compatible
            return FibonacciSequence.Iter.__next__( self)

        def __len__( self): # optional
            return self.size

    def __init__( self, size = 10):
        self.size = size

    def __iter__( self):
        return FibonacciSequence.Iter( self.size)

for v in FibonacciSequence( 8):
    print( v, end = ',')
print()

print( [ v for v in FibonacciSequence( 6)])

# Generator is function with yield statement:
def FibonacciGenerator( count = 10):
    prev, curr = 0, 1
    while count >= 1:
        count -= 1
        yield curr
        prev, curr = curr, curr + prev

# Generators can be used as iterators:
it = FibonacciGenerator( 3)
print( next( it))
print( next( it))
print( next( it))
try:
    print( next( it))
except StopIteration:
    print( 'StopIteration Raised.')

# Check if iterable:
def check( name, obj):
    import sys
    if sys.version_info.major >= 3:
        from collections.abc import Iterable, Iterator, Generator
    else:
        from collections import Iterable, Iterator
    print( name + " is Iterable: " +
                ( 'True' if isinstance( obj, Iterable) else 'False'))
    print( name + " is Iterator: " +
                ( 'True' if isinstance( obj, Iterator) else 'False'))
    if sys.version_info.major >= 3:
        print( name + " is Generator: " +
                    ( 'True' if isinstance( obj, Generator) else 'False'))

check( 'list', [])
check( 'iter()', iter( []))
check( 'range()', range( 10))
check( 'FibonacciSequence', FibonacciSequence())
check( 'FibonacciGenerator', FibonacciGenerator())

# End of 'iterator.py' 

