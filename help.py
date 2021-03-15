#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : help.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-30 18:10 CST(+0800)   
@Brief  :  

'''

# Use help() function to show document of an object (or a funtion):
help( help)
help( str)
help( len)

# DocString for user-defined objects:

def foo( arg1, arg2=None):
    '''
    Foo is an example function.
    :param args1: no use
    :param args2: no use too
    :return: 123
    '''
    return 123

help( foo)

class Bar:
    '''
    Bar is a class that does nothing.
    '''
    def __init__( self):
        pass
    def bar( self):
        '''
        return myself.
        '''
        return self

help( Bar)

# End of 'help.py' 

