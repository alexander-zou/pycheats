#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : control.py   
@Author : alexander.here@gmail.com   
@Date   : 2020-01-13 17:53   
@Brief  :  

'''

def my_exec( statement):
    print( ">>> " + statement)
    exec( statement) # use eval() for expressions

# calc:
my_exec( 'print( 5 / 2)')
my_exec( 'print( 5 // 2)')
my_exec( 'print( 5 % 2)')

# access all variables:
for name in set( locals().keys()): # locals() & globals() are basically dicts
    print( name + " -> " + str( type( locals()[ name])))

# condition:
x = int( input( 'please input an integer: '))
if x < 0:
    print( 'x is negative number')
elif x % 2 == 0:
    print( 'x is even number')
else:
    print( 'x is odd number')

my_exec( 'print( x if x % 2 == 0 else 2 * x)')

# loops:
print( '=== count down ===')
count = 3
while count > 0:
    print( count)
    count -= 1
print( '==================')

print( '==== foreach =====')
for x in [ 2, 3, 5, 7, 13]:
    if x > 10:
        break # & continue works for while too
    print( x)
print( '==================')

# pass - complete structure without actually doing anything:
def noop():
    pass
for i in range( 3):
    pass


# End of 'basic.py' 

