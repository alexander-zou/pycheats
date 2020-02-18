#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : types.py   
@Author : alexander.here@gmail.com  
@Date   : 2020-02-18 16:35   
@Brief  :  

'''

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

# operations:
print( "xyz" + "123")
print( "xyz" * 3)

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

# format string:
print( "\nformat:")
print( "{}, {}".format( "hello", "world"))
print( "{1}: {0}, {1}".format( "hello", "world"))

# c-style format string:
print( "%s, %d, %6.2f" % ( 'xyz', 123, 4.5678))

# End of 'string.py' 

