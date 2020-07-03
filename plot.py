#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : plot.py   
@Author : alexander.here@gmail.com   
@Date   : 2020-04-08 11:34 CST(+0800)   
@Brief  :  

'''

# pip install matplotlib
# more info: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

from __future__ import print_function
import matplotlib.pyplot as plt

x = [ 1, 2, 3]
y1 = [ 2, 4, 1]

# to support CJK charactors:
plt.rcParams[ 'font.sans-serif'] = [ 'SimHei', 'Heiti TC', 'Adobe Heiti Std', 'Adobe Fan Heiti Std']

plt.plot( x, y1)
#plt.xlabel('x - axis') 
#plt.ylabel('y - axis')
#plt.title('My Graph')
#plt.grid( True)
print( "Press 'Q' to continue ...")
plt.show()

y2 = [ 4, 1, 3]
plt.plot( x, y1, label = 'line 1')
plt.plot( x, y2, label = 'line 2')
plt.legend()
print( "Press 'Q' to continue ...")
plt.show()

# End of 'plot.py' 

