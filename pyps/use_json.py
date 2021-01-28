#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_json.py 
@Author : alexander.here@gmail.com
@Date   : 2020-04-13 11:47 CST(+0800)   
@Brief  :  

'''

import json

data = {
    'STR': 'this is a string',
    'integer': 123,
    'float': 456.789,
    'boolean' : True,
    'list' : [ i for i in range( 10)],
    'dict' : { 1: 2, 3: 4, 5: 6},
}

# IO:
encoded = json.dumps( data)
loaded = json.loads( encoded)

# Print:
print( json.dumps( loaded, indent = 16, sort_keys = True))

# End of 'use_json.py' 

