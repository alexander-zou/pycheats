#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_pyinstaller.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2022-10-09 16:04    (+0800)   
@Brief  :  

'''

# See https://pyinstaller.org/en/stable/usage.html for more info.

def ConvertPNG2ICO():
    from PIL import Image
    Image.open( 'app.png').save( 'app.ico')

def PackExecutable():
    import os
    os.system( 'pyinstaller -w -F use_pyinstaller.py --icon app.ico --add-data "app.ico;."')
    # '-w' for window-only, terminal outputs will not show up.
    # '-F' for one-file package, no extra data files needed.
    # '--icon' for icon of executable file. Will NOT effect on tkinter windows!
    # '--add-data "AAA;BBB"' to add file 'AAA' to runtime folder 'BBB'.
    #               For Non-Windows systems, change ';' for ':', or simply use os.pathsep .

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

