#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_csv.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-28 12:05 CST(+0800)   
@Brief  :  

'''

import csv, sys

# Simple use:
with open( 'use_csv.csv', 'r') as file:
    reader = csv.reader( file)
    for row in reader:
        print( list( row))

# Detect dialect:
with open( 'use_csv.csv', 'r') as file:
    dialect = csv.Sniffer().sniff( file.read())
    file.seek( 0)
    reader = csv.reader( file, dialect)
    for row in reader:
        print( list( row))

# Avoid common decoding/parsing errors:
if sys.version_info.major >= 3: # (Python3 ONLY!)
    with open( 'use_csv.csv', 'r',
                encoding = 'utf-8', # Change if neede
                errors = 'ignore') as csv_file:
        reader = csv.reader( ( line.replace('\0','') for line in csv_file))
        for row in reader:
            print( list( row))

# Load from memory (instead of file):
if sys.version_info.major == 2:
    from StringIO import StringIO
elif sys.version_info.major >= 3:
    from io import StringIO
data = u'''\
"Title","Column 1",Column 2
xxx,1.23,4.56
"yyy",7,8
'''
wrapped_string = StringIO( data)
reader = csv.reader( wrapped_string)
for row in reader:
    print( list( row))

# End of 'use_csv.py' 

