from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

# recurring_checkbox.py contains style and config information for the make recurring checkbox

def make_recurring_style_gen():
    make_recurring = ttk.Style()
    make_recurring.configure(
        'Recurring.TCheckbutton',
        foreground='black',
        background='DeepSkyBlue'
    )
    return 'Recurring.TCheckbutton'

def make_recurring_checkbox_gen(frame, bool_var):
    recurring_checkbox = Checkbutton(
        frame,
        text='Make Recurring',
        variable=bool_var,
        onvalue=1,
        offvalue=0,
        style=make_recurring_style_gen()
    )
    return recurring_checkbox