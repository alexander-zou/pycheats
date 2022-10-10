#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_pyinstaller.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2022-10-09 16:04    (+0800)   
@Brief  :  

'''

def ConvertPNG2ICO():
    from PIL import Image
    Image.open( 'app.png').save( 'app.ico')

def PackEXE():
    import os
    os.system( 'pyinstaller -w -F use_pyinstaller.py --icon app.ico --add-data "app.ico;."')

if __name__ == '__main__':
    import os, pathlib, tkinter

    window = tkinter.Tk() # Create main window
    window.title( 'Pyinstaller Demo')
    window.geometry( '400x200')
    
    # To make sure packed files(e.g. 'app.ico') can be found:
    mydir = pathlib.Path( __file__).parent.resolve()
    window.iconbitmap( os.path.join( mydir, 'app.ico'))

    tkinter.Label( text='Hello PyInstaller !').pack( fill=tkinter.BOTH, expand=True)
    window.mainloop()

# End of 'use_pyinstaller.py' 

