#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Copyright (c) 2021 JIIOV. All Rights Reserved

@File   : class.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-02-01 10:43 CST(+0800)   
@Brief  :  

'''

# Basic Define:

class ClassName:
    # Class Member / Static Variable:
    Instances = []

    # Constructor:
    def __init__( self, other_args):
        self.data_member = other_args
        ClassName.Instances.append( self)
    
    # Methods:
    def show( self): # 1st arg must be self
        print( self.data_member)
    
    # Class Method / Static Function:
    @classmethod
    def ShowAll( cls): # 1st arg must be class
        print( 'ShowAll() called from %s' % ( cls))
        for obj in ClassName.Instances:
            obj.show()

    @staticmethod
    def Count():
        return len( ClassName.Instances)


# Basic Use:

ClassName( 0)
ClassName( 1)
obj = ClassName( 2)
obj.show()
print( '%d instances totally.' % ( ClassName.Count()))
ClassName.ShowAll()


# Reflection:

print( 'obj is instance of ClassName:', isinstance( obj, ClassName))
print( 'type: ', type( obj), ClassName) # type( obj) equals ClassName
print( 'class contents: ', dir( obj)) # dir() returns string names of class contant
# getattr( cls, name) retrieves actual object inside class by name:
print( 'methods: ', [ m for m in dir( ClassName) if callable( getattr( ClassName, m))])
getattr( ClassName, 'ShowAll')()

print( 'Call bound method:')
bound_method = getattr( obj, 'show')
bound_method()
print( 'Call unbound method:')
unbound_method = getattr( ClassName, 'show')
unbound_method( obj)


# OO / Inheriting:

class Derived( ClassName):
    def __init__( self, arg='derived_member'):
        self.derived_member = arg
        # use super() to get super class instance:
        super().__init__( 888)
    
    # Override:
    def show( self):
        print( self.data_member, self.derived_member)

obj = Derived()
print( 'Classmethod and Staticmehod are inherited:')
print( Derived.Count())
Derived.ShowAll()
print( 'is sub class:', issubclass( Derived, ClassName))

# Check out for more: https://docs.python.org/3/tutorial/classes.html

# End of 'class.py' 

