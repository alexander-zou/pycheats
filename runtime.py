#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Copyright (c) 2020 Face++, Megvii. All Rights Reserved

@File   : runtime.py   
@Author : zoujiachen@megvii.com   
@Date   : 2020-03-24 11:02 CST(+0800)   
@Brief  :  

'''

# get python3's function vertion of print in python2:
from __future__ import print_function

import sys

# get python version:
major_ver = sys.version_info.major
minor_ver = sys.version_info.minor
patch_ver = sys.version_info.micro
# also:
major_ver = sys.version_info[ 0]
minor_ver = sys.version_info[ 1]
patch_ver = sys.version_info[ 2]

# process name & arguments:

for idx, arg in enumerate( sys.argv):
    print( 'argument #%d: %s' % (idx, arg))

# End of 'runtime.py' 

