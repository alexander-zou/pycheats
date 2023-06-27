#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : strings.py   
@Author : alexander.here@gmail.com  
@Date   : 2020-02-18 16:35   
@Brief  :  

'''

import sys

# string literals:
s1 = "Hello, 'World\" !"
s2 = 'Hello, \'World" !'
print( id( s1))
print( id( s2))

long_string = '''
this is a very long string.
a long string can contain many lines.
'''

# methods:
print( s1.upper()) # upper() and lower() methods return new object
print( s1.isupper())

idx1 = s2.index( "'") # raise error if not found
idx2 = s2.find( '"') # return -1 if not found
print( s2[ idx1 : idx2 + 1]) # [START:END] or [START:END:STEP], empty for default

print( "replace 'o' to '*' : " + s1.replace( 'o', '*'))

# check if contains:
my_string = 'my string'
my_pattern = 'ing'
if my_pattern in my_string:
    print( "'" + my_string + "' contains '" + my_pattern + "'.")

# operations:
print( "xyz" + "123")
print( "xyz" * 3)

# join:
print( 'X'.join( ( 'A', 'B', 'C')))
print( ''.join( [ 'P', 'y', 't', 'h', 'o', 'n']))

# regex expersion:

import re

print( "\nre.search:")
result = re.search( '\'([A-Z]+)(.*)\"', s1)
if result:
    print( 'start:', result.start())
    print( 'group 0:', result.group( 0))
    print( 'group 1:', result.group( 1))
    print( 'group 2:', result.group( 2))

# re.match() is similar with re.search, but require a whole string match.

print( "\nfindall:")
pattern = re.compile( '^[a-z]+\\s+[a-z]+', re.I | re.M ) # re.M for multiline
for m in pattern.findall( long_string):
    print( m)

# Split string with regex as delimiter:
print( re.split( ',|;|\.|\s', 'hello,world.hello program'))

# format string:
print( "\nformat:")
print( "{}, {}".format( "hello", "world"))
print( "{1}: {0}, {1}".format( "hello", "world"))

# c-style format string:
print( "%s, %d, %6.2f" % ( 'xyz', 123, 4.5678))

# f-string:
if ( sys.version_info.major, sys.version_info.minor) >= ( 3, 6):
    x = 259
    print( f"sqrt({x}) = {x**0.5} ≈ {x**0.5:.3f}\n{x} in hexadecimal is {x:#06x}\njust a left brace character: {{")

# End of 'strings.py' 

