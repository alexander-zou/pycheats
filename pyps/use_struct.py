#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_struct.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-28 17:31 CST(+0800)   
@Brief  :  

'''

# more info: https://docs.python.org/3/library/struct.html

import struct as s

# struct {
#   uint16_t x, y;
#   int32_t z;
#   float f;
# };

binary_data = s.pack( 'HHif', 1, 2, 3, 4.56)
print( s.unpack( 'HHif', binary_data))

# Common data type flags:
#   Flag    C-Type          Bytes
#   b       signed char     1
#   B       unsigned char   1
#   h       short           2
#   H       unsigned short  2
#   i       int             4
#   I       unsigned        4
#   f       float           4
#   d       double          8


# Toggle endianness:
binary_data = s.pack( '<HH', 255, 256)
print( s.unpack( '>HH', binary_data))

# Endianness flags:
#   '<' little-endian
#   '>' big-endian
#   '=' native implementation

# End of 'use_struct.py' 

