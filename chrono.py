#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : chrono.py   
@Author : alexander.here@gmail.com  
@Date   : 2020-01-13 15:00   
@Brief  :  

'''

import time

now = time.time() # unix epoch time in seconds
lt = time.localtime( now)

# timestamp:
print( "timestamp: %fms" % ( now * 1000))

# format:
print( "formated: " + time.strftime( '%Y-%m-%d %H:%M:%S %Z', lt)) # man strftime for more

# parsing:
print( "Year:", lt.tm_year)
print( "Month:", lt.tm_mon)
print( "Day in Month:", lt.tm_mday)
print( "Hour:", lt.tm_hour)
print( "Minute:", lt.tm_min)
print( "Second:", lt.tm_sec)
print( "Day in Year:", lt.tm_yday)
print( "Day in Week:", lt.tm_wday)
print( "Daylight Saving Time:", lt.tm_isdst)




# End of 'chrono.py' 

