#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time

TOTAL = 200

def SimpleProgress():
    for p in range( TOTAL + 1):
        time.sleep( 0.01)
        print( "\rProgress: %.0f%%" % ( p / TOTAL * 100), end = '', flush = True)
        # for python2.7, use 'sys.stdout.flush()'
    print( ' DONE.') # make sure print new line

def UseTqdm():
    try:
        from tqdm import tqdm
        for i in tqdm( range( TOTAL)):
        # utilize argument 'total=' for iterators which don't have the __len__() method
            time.sleep( 0.01)
            # do somethine with i
    except ModuleNotFoundError:
        print( "Need to install tqdm module first !!!")

print( "Simple:")
SimpleProgress()

print( "tqdm:")
UseTqdm()



