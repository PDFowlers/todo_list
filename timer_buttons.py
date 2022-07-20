from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

# timer_buttons.py contains style and config settings for the start and reset timer buttons

def start_timer_style_gen():
    start_timer_style = ttk.Style()
    start_timer_style.configure(
        'Start.TButton',
        background='green2',
        font=('times 14'),
        padx=20,
        pady=10,
        relief='raised',
        bordercolor='green2'
    )
    return 'Start.TButton'

def start_timer_gen(frame, cmd):
    start_timer = Button(
        frame,
        text='Start Timer',
        command=cmd,
        style=start_timer_style_gen()
    )
    return start_timer

def reset_timer_style_gen():
    reset_timer_style = ttk.Style()
    reset_timer_style.configure(
        'Reset.TButton',
        background='red',
        font=('times 14'),
        padx=20,
        pady=10
    )
    return 'Reset.TButton'

def reset_timer_gen(frame, cmd):
    reset_timer = Button(
        frame,
        text='Reset Timer',
        command=cmd,
        style=reset_timer_style_gen()
    )
    return reset_timer
