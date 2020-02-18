#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : exception.py   
@Author : alexander.here@gmail.com
@Date   : 2020-01-13 12:37   
@Brief  :  

'''

print( "Catch any error:")
try :
    kldsjaflkdjsf
    adfasdk23ri2g0o
    rf23wrf( 45)
except:
    pass

print( "Catch different types of errors:")
try :
    data = int( input( "Please enter a number:"))
    print( "reciprocal number is " + str( 1.0 / data))
except KeyboardInterrupt: # Ctrl-C
    print( "Canceled.")
except ( ZeroDivisionError, NameError, ValueError):
    print( "Invalid Input!!!")
except:
    print( "Other ERROR!!!")
finally:
    print( "Finally statements will always be executed")

print( "Create, raise, process exceptions:")
try :
    # Exception can be create as normal objects:
    raise NameError( 'this is error message')
except Exception as e: # parse more info from Exception objects:
    print( "type of exception: " + str( type( e)))
    print( "string of exception: " + str( e))
    print( "====== trace back =======")
    import traceback
    print( traceback.format_exc())
    print( "=== end of trace back ===")

# User-defined exceptions should derive from exception:
class MyError( Exception): # ends with 'Error' as naming convention
    def __init__( self, arg1, arg2, arg3):
        self.arg1, self.arg2, self.arg3 = arg1, arg2, arg3



# End of 'exception.py' 

