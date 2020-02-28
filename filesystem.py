#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : filesystem.py   
@Author : alexander.here@gmail.com   
@Date   : 2020-01-13 15:53   
@Brief  :  

'''

# see https://docs.python.org/3/library/pathlib.html for OO-style path handling

import os
import tempfile
import shutil

# PWD, current path:
path = os.path.curdir
print( "pwd: " + path)

# absolute path:
path = os.path.abspath( path)
print( "absolute pwd: " + path)

#dirname:
print( "dirname: " + os.path.dirname( path))

# basename:
path = os.path.basename( path)
print( "basename: " + path)

# create temp dir:
base_path = tempfile.mkdtemp()
print( "temp dir created: " + base_path)

# join path:
dir1 = os.path.join( base_path, 'some/parent/dir1')
print( "path of dir1: " + dir1)

# make folder with parent:
os.makedirs( dir1, 0o777, exist_ok = True) # NEED PYTHON3 !!!
# raise Error when path existed if exist_of = False

dir2 = os.path.join( dir1, '..', 'dir2')
print( "path of dir2: " + dir2)

# normal mkdir:
os.mkdir( dir2)

# write file:
file1 = os.path.join( dir1, "file1.txt")
with open( file1, 'w') as f:
    f.write( "hello, world!\n")
    f.write( "2nd line here.\n")

# copy file:
file2 = os.path.join( dir2, "file2.txt")
shutil.copy( file1, file2)

# also:
# shutil.move( file1, file2) # move/rename file
# shutil.copy2( file1, file2) # copy file like 'shutil.copy()', while preserving metadata like 'cp -p'
# shutil.copytree( src, dst) # copy folder like 'cp -r'

# read file:
with open( file2, 'r') as f:
    print( '==== Content of file2.txt ====')
    print( f.read())
    print( '==============================')

# common path:
print( "common path of '" + file1 + "' & '" + file2 + "' : " + os.path.commonpath( ( file1, file2)))

# rename file:
file3 = os.path.join( dir2, "file3.txt")
os.rename( file2, file3)

# travel tree:
print( "traveling '" + base_path + "' ...")
for base, folders, files in os.walk( base_path):
    # insure travel order (optional) :
    folders.sort(); files.sort()
    print( "current: " + base)
    print( "files: " + str( files))
    print( "folders: " + str( folders))

# delete tree (like rm -rf):
shutil.rmtree( base_path)
print( "temp dir tree removed: " + base_path)

# End of 'filesystem.py' 

