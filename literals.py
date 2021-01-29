#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : literals.py   
@Author : alexander.here@gmail.com
@Date   : 2020-04-16 13:19 CST(+0800)   
@Brief  :  

'''

# BOOL literals:
True
False

# int literals:
0
1
2
int( '1000', base = 2) # binary
int( '0010', base = 8) # octonary
int( 'ff', base = 16)  # hexadecimal
int( '0xff', base = 16)# same as above

# float literals:
0.0
0.1
0.2
float( 'inf')
float( '+inf') # same as above
float( '-inf')
float( 'nan')

# string literals:
'string'
"string"

long = '''\
this is a very long string.
a long string can contain many lines.'''

print( long)

# End of 'literals.py' 

