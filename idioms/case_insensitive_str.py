#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
@File   : case_insensitive_str.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2024-02-21 10:47    (+0800)   
@Brief  :  

'''

class CaseInsensitiveStr( str):
    def __new__( cls, string):
        return super().__new__( cls, string)
    def __eq__( self, other):
        if isinstance( other, str):
            return self.lower() == other.lower()
        return super().__eq__( other)
    def __ne__( self, other):
        return not self.__eq__( other)
    def __hash__( self):
        return hash( self.lower())

def show_value( exp:str):
    print( f'{exp:56} -> [{eval(exp)}]')

instance = CaseInsensitiveStr( "Hello, world!")

show_value( "instance")
show_value( "instance == 'hello, WORLD!'")
show_value( "instance != 'Hello, world?'")

amount = {
    CaseInsensitiveStr( 'K9') : 100,
    CaseInsensitiveStr( 'Cat') : 1,
}
amount[ 'k9'] += 1
amount[ 'CAT'.lower()] = 9 # use lower() to make sure hash keys are same!

show_value( "amount")


# End of 'case_insensitive_str.py' 

