#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : date_and_time.py   
@Author : alexander.here@gmail.com
@Date   : 2020-04-08 15:44 CST(+0800)   
@Brief  :  

'''

# more info: https://docs.python.org/3/library/time.html

from __future__ import print_function

import time

print( 'current timestamp:', time.time())
print( 'local time struct:', time.localtime()) # time.localtime() == time.localtime( time.time())
print( 'asctime:', time.asctime( time.localtime()))
print( 'formated time:', time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime()))

import calendar

print( 'Calendar:')
print( calendar.calendar( 2000))
if calendar.isleap( 2000):
    print( 'Year 2000 is leap year!')

# End of 'date_and_time.py' 

