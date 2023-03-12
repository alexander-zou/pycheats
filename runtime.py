#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : runtime.py   
@Author : zoujiachen@megvii.com   
@Date   : 2020-03-24 11:02 CST(+0800)   
@Brief  :  

'''

# get python3's function vertion of print in python2:
from __future__ import print_function

# get dict that contains all variables and functions currently in envirment:
print( vars())

import os, sys

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

# tell which OS:
if sys.platform == 'win32':
    print( 'Using Windows.')
elif sys.platform == 'darwin':
    print( 'Using MacOS')
elif sys.platform.startswith == 'linux':
    print( 'Using Linux')

# run shell command:

if os.name != 'posix':
    cmd = 'ver'
else:
    cmd = 'uname -a'
print( 'Running command: ' + cmd)
ret = os.system( cmd)
print( "returned: %d" % ( ret))

print( 'Running command: ' + cmd)
stream = os.popen( cmd) # or: with os.popen( cmd) as stream
print( "Command Output:")
print( stream.read())
stream.close()


# import from path:
path = 'strings.py'
module_name = 'strings'
if sys.version_info.major <= 2:
    import imp
    module = imp.load_source( module_name, path)
elif sys.version_info.minor <= 4:
    from importlib.machinery import SourceFileLoader
    module = SourceFileLoader( module_name, path)
else:
    import importlib.util
    spec = importlib.util.spec_from_file_location( module_name, path)
    module = importlib.util.module_from_spec( spec)
    spec.loader.exec_module( module)
print( module.long_string)

# environment:
os.environ[ 'ABC'] = "XYZ"                  # set env
print( 'env: ABC=' + os.environ[ 'ABC'])    # get env
os.putenv( 'ABC', '123')    # set env for subprocesses
print( 'cur-process : ABC=' + os.environ[ 'ABC'])
os.system( 'bash -c "echo sub-process : ABC=$ABC"')

# End of 'runtime.py' 

