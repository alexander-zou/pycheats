#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_subprocess.py   
@Author : zouji   
@Date   : 2023-03-12 12:50    (+0800)   
@Brief  :  

'''

# see https://docs.python.org/3/library/subprocess.html for detailed info.

import subprocess

# run command:
subprocess.run( [ 'ls', '-l'])

# get results:
ret = subprocess.run( 'uname', capture_output=True)
print( 'ret:', ret.returncode)
print( 'stdout:', ret.stdout)
print( 'stderr:', ret.stderr)

# other args:
subprocess.run( ['env'], cwd='.', env={ 'x':'123'}, timeout=0.5, check=True)
#   cwd: current working directory
#   env: str->str map
#   timeout: raise exception if time expired
#   check: raise exception if return code is NOT 0

# async:
p = subprocess.Popen( [ 'sleep', '1'])
print( 'subproecss started!')
p.wait() # or p.wait( timeout=2)
print( 'subproecss fineshed:', p.returncode)


# End of 'use_subprocess.py' 

