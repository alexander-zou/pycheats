#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_tkinter.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2022-10-09 11:57    (+0800)   
@Brief  :  

'''

import tkinter

def Demo_QuickStart():
    window = tkinter.Tk() # Create main window
    window.title( 'Tkinter Demo')
    
    # Create tkinter variables:
    value_a = tkinter.DoubleVar( value=0.0)
    value_b = tkinter.DoubleVar( value=0.0)
    value_result = tkinter.DoubleVar( value=0.0)
    
    # callback:
    def calc_result():
        sum = value_a.get() + value_b.get()
        value_result.set( sum)
    
    # widgets layout:
    tkinter.Entry( master=window, textvariable=value_a).pack( side=tkinter.LEFT)
    tkinter.Label( master=window, text=" + ").pack( side=tkinter.LEFT)
    tkinter.Entry( master=window, textvariable=value_b).pack( side=tkinter.LEFT)
    tkinter.Button( master=window, text=" = ", command=calc_result).pack( side=tkinter.LEFT)
    tkinter.Entry( master=window, textvariable=value_result).pack( side=tkinter.LEFT)
    
    # Start mainloop:
    window.mainloop()

def Demo_Widgets():
    window = tkinter.Tk()
    window.title( 'Tkinter Demo 2')
    
    frame_upper = tkinter.Frame( window)
    frame_upper.pack( side=tkinter.TOP, fill=tkinter.X)
    
    # upper-left area:
    frame_upper_left = tkinter.Frame( frame_upper)
    frame_upper_left.pack( side=tkinter.LEFT)
    
    check_button_value = tkinter.BooleanVar()
    tkinter.Checkbutton( frame_upper_left, text="CheckButton", variable=check_button_value).pack( side=tkinter.TOP)
    tkinter.Label( frame_upper_left, textvariable=check_button_value).pack( side=tkinter.TOP)
    
    radio_button_value = tkinter.IntVar()
    tkinter.Radiobutton( frame_upper_left, text="Radio 1", value=1, variable=radio_button_value).pack( side=tkinter.TOP)
    tkinter.Radiobutton( frame_upper_left, text="Radio 2", value=2, variable=radio_button_value).pack( side=tkinter.TOP)
    tkinter.Radiobutton( frame_upper_left, text="Radio 3", value=3, variable=radio_button_value).pack( side=tkinter.TOP)
    tkinter.Label( frame_upper_left, textvariable=radio_button_value).pack( side=tkinter.TOP)
    
    scale_value = tkinter.DoubleVar()
    tkinter.Scale( frame_upper_left, from_=0.0, to=1.0, digits=4, resolution=0.04, orient=tkinter.HORIZONTAL, variable=scale_value).pack( side=tkinter.TOP)
    
    spinbox_value = tkinter.StringVar()
    tkinter.Spinbox( frame_upper_left, values=( 'Option1', 'Option2', 'Option3'), textvariable=spinbox_value).pack( side=tkinter.TOP)
    tkinter.Label( frame_upper_left, textvariable=spinbox_value).pack( side=tkinter.TOP)
    
    # upper-right area:
    frame_upper_right = tkinter.Frame( frame_upper, padx=4, pady=4)
    frame_upper_right.pack( side=tkinter.RIGHT, fill=tkinter.BOTH, expand=tkinter.YES)
    
    listbox = tkinter.Listbox( frame_upper_right, selectmode=tkinter.EXTENDED)
    listbox.pack( side=tkinter.RIGHT, fill=tkinter.BOTH, expand=tkinter.YES)
    for item in [ 'Item A', 'Item B', 'Item C', 'Item D']:
        listbox.insert( tkinter.END, item)
    
    def on_listbox_changed( event):
        global listbox
        print( listbox.curselection())
    listbox.bind( '<<ListboxSelect>>', on_listbox_changed)
    
    # lower area:
    frame_lower = tkinter.Frame( window)
    frame_lower.pack( side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=tkinter.YES)
    
    scrollbar = tkinter.Scrollbar( frame_lower)
    scrollbar.pack( side=tkinter.RIGHT, fill=tkinter.Y)
    text = tkinter.Text( frame_lower)
    text.pack( side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
    scrollbar.config( command=text.yview)
    text.config( yscrollcommand=scrollbar.set)
    
    text.insert( tkinter.INSERT, """\
The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and \
tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.\

Tkinter supports a range of Tcl/Tk versions, built either with or without thread support. The official Python \
binary release bundles Tcl/Tk 8.6 threaded. See the source code for the _tkinter module for more information \
about supported versions.\

Tkinter is not a thin wrapper, but adds a fair amount of its own logic to make the experience more pythonic. \
This documentation will concentrate on these additions and changes, and refer to the official Tcl/Tk documentation \
for details that are unchanged.\
""")
    
    window.mainloop()

def Demo_Dialogs():
    import tkinter.messagebox
    tkinter.messagebox.showerror( title='Error Title', message='Error Messsage')
    print( tkinter.messagebox.askyesno( title='Question', message='Please choose yes or no'))
    # more about: https://docs.python.org/3/library/tkinter.messagebox.html

    import tkinter.colorchooser
    print( tkinter.colorchooser.askcolor())

    import tkinter.filedialog
    filetypes = [
        ('PNG Image', '*.png'),
        ('JPEG Image', '*.jpg;*.jpeg'),
        ('ALL','*.*')]
    print( tkinter.filedialog.asksaveasfilename( title='Save As', filetypes=filetypes))
    # more about: https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog

    import tkinter.simpledialog
    name = tkinter.simpledialog.askstring( title='Please Enter', prompt='Name')
    age = tkinter.simpledialog.askinteger( title='Please Enter', prompt='Age')
    print( name, age)
    # more about: https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog

    # Customized Simple Dialog:
    class MyDialog( tkinter.simpledialog.Dialog):
        def __init__( self, parent=None): # should no parent assigned, super() will create a temporary toplevel
            self.ok_pressed = False
            super().__init__( parent, 'My Dialog Title')
        def on_ok( self):
            try:
                self.enter_age.get()
            except:
                tkinter.messagebox.showerror( title='Error', message='Invalid Input!')
                return
            self.ok_pressed = True
            self.destroy()
        def body( self, master):
            # init tkinter variables here to ensure we have toplevel window now:
            self.enter_name = tkinter.StringVar( value='Jane Doe', master=master)
            self.enter_age = tkinter.IntVar( value=18, master=master)
            frame1 = tkinter.Frame( master)
            frame1.pack( side=tkinter.TOP, fill=tkinter.X, padx=2, pady=2)
            tkinter.Label( frame1, text='Name:', width=10).pack( side=tkinter.LEFT)
            tkinter.Entry( frame1, textvariable=self.enter_name).pack( side=tkinter.RIGHT, fill=tkinter.X)
            frame2 = tkinter.Frame( master)
            frame2.pack( side=tkinter.TOP, fill=tkinter.X, padx=2, pady=2)
            tkinter.Label( frame2, text=' Age:', width=10).pack( side=tkinter.LEFT)
            tkinter.Entry( frame2, textvariable=self.enter_age).pack( side=tkinter.RIGHT, fill=tkinter.X)
        def buttonbox( self):
            tkinter.Button( self, text='Cancel', width=8, command=self.destroy).pack( side=tkinter.RIGHT, padx=18, pady=6)
            tkinter.Button( self, text='Ok', width=8, command=self.on_ok).pack( side=tkinter.RIGHT, padx=18, pady=6)
            self.bind("<Return>", lambda event: self.on_ok())
            self.bind("<Escape>", lambda event: self.destroy())
    my_dialog = MyDialog( None)
    if my_dialog.ok_pressed:
        print( my_dialog.enter_name.get(), my_dialog.enter_age.get())
    # more aboug: https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog

if __name__ == '__main__':
    Demo_QuickStart()
    Demo_Widgets()
    Demo_Dialogs()
    pass

# References:
#   Offical Document - https://docs.python.org/3/library/tkinter.html
#   Quick Tutorial - https://www.runoob.com/python/python-gui-tkinter.html
#   About Layouts - https://redhuli.io/pack-place-and-grid-in-tkinter/
#   Drag&Drop Wrapper - https://github.com/Eliav2/tkinterdnd2


# End of 'use_tkinter.py' 

