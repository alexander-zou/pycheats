#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : unzip.py   
@Author : alexander.here@gmail.com  
@Date   : 2020-02-27 12:38 CST(+0800)   
@Brief  :  

'''

# See https://docs.python.org/zh-cn/3/library/zipfile.html for more info.

from zipfile import ZipFile
import os

# Extract ALL files at once:

with ZipFile( 'pack.zip') as zipObj:
    zipObj.extractall( 'output_folder') # output folders will be created if not exists

######################### !!! IMPORTANT !!! #################################
# extractall WON'T work properly with non-ascii charactors within path !!!  #
#############################################################################



# Extract files one by one ( with proper path decoding ) :

output_path = 'output_folder'
with ZipFile( 'pack.zip') as zipObj:
    for raw_path in zipObj.namelist(): # namelist() is ordered
        if raw_path[:9] == '__MACOSX/':
            continue
        real_path = raw_path.encode( 'cp437').decode( 'utf-8') # for python3
        # real_path = raw_path.decode( 'utf-8') # for python2
        if zipObj.getinfo( raw_path).is_dir():
            dir_name = os.path.join( output_path, real_path)
            os.makedirs( dir_name, exist_ok=True)
        else :
            full_output_path = os.path.join( output_path, real_path)
            with zipObj.open( raw_path) as one_packed_file: # to write data, call with mode='w'
                with open( full_output_path, 'wb') as output_file:
                    output_file.write( one_packed_file.read())



# End of 'unzip.py' 

