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

from datetime import datetime
unix_ts = 1577927552.593
print( 'converted time:', datetime.fromtimestamp( unix_ts))
ts = datetime.strptime( "2001-02-28 11:59:01", "%Y-%m-%d %H:%M:%S")
# or ts = datetime( 2001, 2, 28, 11, 59, 1)
print( 'strftime: ' + ts.strftime( "%Y-%m-%d %H:%M:%S"))

import calendar

print( 'Calendar:')
print( calendar.calendar( 2000))
if calendar.isleap( 2000):
    print( 'Year 2000 is leap year!')

# End of 'date_and_time.py' 

