#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : datatype.py   
@Author : alexander.here@gmail.com  
@Date   : 2020-01-13 18:36   
@Brief  :  

'''

import sys

# type() function:
print( type( 1), type( 1.2), type( 'hello'),
        type( ( 1, 2, 3)), type( [ 1, 2, 3]), type( { 1, 2, 3}),
        type( { 1:2, 3:4}))

# check type with inheritance relationships considered:
if isinstance( 1, int):
        print( "isinstance( 1, int)")

# type is a type:
print( int, float, str, tuple, list, set, dict)
print( None, type( None), type( type( None)))

# conversion:
my_type = str
print( type( my_type( 123)))

# sample code for list:
a_list = [ 0, 1, 2, 3, 4, 5, 6, 8]
a_list.remove( 8) # remove first match
a_list.append( 7)
print( a_list[ 1::2]) # [START:END] or [START:END:STEP], empty means default

del a_list[ 0:2] # same with : del a_list[ 0]; del a_list[ 1]
a_list.reverse() # in-place reverse
print( a_list)

# added in python 3.3:
another_list = a_list.copy()
a_list.clear()
print( another_list[ ::-1])

# make list with for statement (List Comprehension):
print( [ x * 2 + 1 for x in range( 10, 15)])

# sample code for tuple:
a_tuple = ( 'fine.', 'thanks.', 'and you?')
print( a_tuple[ 1])
# a tuple is basically an immutable list.

# one can ofter leave brackets out of a tuple:
a_tuple = 1, # NOTE: at least 1 comma must be presented
print( type( a_tuple))

# sample code for set:
a_set = { 1, 2, 3}
a_set.remove( 2)
a_set.add( 5)
print( a_set)
a_set.clear()

# sample code for dict:
a_dict = { 'hello' : 'hi', 'thanks' : 'you\'re welcome'}
a_dict[ 'how are you'] = 'fine' # add / modify
del a_dict[ 'thanks'] # remove

if sys.version_info.major >= 3:
        for key, value in a_dict.items():
                print( key + " => " + value)

# make dict with for statement (Dictionary Comprehension):
another_dict = { f"square root of {i}" : f"{i**0.5:.3f}" for i in range( 5)}

# merging:
a_dict.update( another_dict)
print( a_dict)

# remove all elements:
a_dict.clear()

# use len() to find size of container:
print( len( a_list), len( a_tuple), len( a_set), len( a_dict))



# End of 'datatype.py' 

