#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : nature_sort.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2022-10-09 11:13    (+0800)   
@Brief  :  

'''

import re
key = lambda x:[int(seg) if seg.isdigit() else seg.lower() for seg in re.split( '(\d+)', x)]

l = [
    'data028-ZZZ',
    'data10_a',
    'data11_b',
    'data7_C',
    'data1_A',
    'data8_B',
    'data8_a',
    'data0_2022-10-1',
    'data0_2022-10-02',
    'data0_2022-9-30']
l.sort( key=key)
print( '\n'.join( l))

# End of 'nature_sort.py' 

