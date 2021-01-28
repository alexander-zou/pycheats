#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_matplotlib.py
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
# to avoid that fonts don't have unicode-minus:
plt.rcParams[ 'axes.unicode_minus'] = False

# Simple Use:
plt.plot( x, y1)
print( "Press 'Q' to continue ...")
plt.show()

# More Customization:
y2 = [ 4, 1, 3]
plt.plot( x, y1, label = 'line 1', marker = '^', color = '#bbf90f', linestyle = '-.')
plt.scatter( x, y2, label = 'line 2', marker = 'x', color = 'red')
# common markers: '^', 'x', 'd', '+', 'o', 'v', 's', '<', '1', '*', '>', 'h'
# common linestyles: '--', '-.', ':', '.', 'o', 'p', '|', '_'
plt.xlabel('x - axis') 
plt.ylabel('y - axis')
plt.title('My Graph')
plt.grid( True)
plt.legend()
print( "Press 'Q' to continue ...")
plt.show()

# Histgram:
datas = [ 1, 5, 2, 4, 5, 9, 3, 5, 7, 5, 7, 4, 6]
plt.hist( datas, bins = 4, color = 'y') # split into 4 bins
plt.hist( datas, bins = range( 10), color = 'b') # define edge of each bin as 0,1,..,9
print( "Press 'Q' to continue ...")
plt.show()

# 3D:
from mpl_toolkits import mplot3d
try:
    import numpy as np
    x = y = np.linspace( -6, 6, 30)
    X, Y = np.meshgrid( x, y)
    Z = np.sin( np.sqrt( X ** 2 + Y ** 2))
    ax = plt.axes(projection='3d')
    ax.plot_surface( X, Y, Z, rstride=1, cstride=1,
                     cmap='viridis', edgecolor='none')
    print( "Press 'Q' to continue ...")
    plt.show()
except:
    print( 'need numpy for 3D plotting demo.')
    pass

# End of 'use_matplotlib.py' 

