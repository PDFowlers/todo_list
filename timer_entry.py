from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

# timer_entry.py contains the configuration for the timer labels and entry fields

def hr_label_style_gen():
    hr_label_style = Style()
    hr_label_style.configure('Hr_Label.TLabel', background='DeepSkyBlue', font=('times, 12'))
    return 'Hr_Label.TLabel'

def hr_label_gen(frame):
    hr_label = Label(frame, style = hr_label_style_gen(), text = 'hours')
    return hr_label

def hr_entry_gen(frame, unit_of_time):
    hr_entry = Entry(frame, textvariable=unit_of_time, width=2, font=('times, 12'))
    return hr_entry

def min_label_style_gen():
    min_label_style = Style()
    min_label_style.configure('Min_Label.TLabel', background='DeepSkyBlue', font=('times, 12'))
    return 'Min_Label.TLabel'

def min_label_gen(frame):
    min_label = Label(frame, style=min_label_style_gen(), text='min', background='DeepSkyBlue')
    return min_label

def min_entry_gen(frame, unit_of_time):
    min_entry = Entry(frame, textvariable=unit_of_time, width=2, font=('times, 12'))
    return min_entry

def sec_label_style_gen():
    sec_label_style = Style()
    sec_label_style.configure('Sec_Label.TLabel', background='DeepSkyBlue', font=('times, 12'))
    return 'Sec_Label.TLabel'

def sec_label_gen(frame):
    sec_label = Label(frame, style=sec_label_style_gen(), text='sec', background='DeepSkyBlue')
    return sec_label

def sec_entry_gen(frame, unit_of_time):
    sec_entry = Entry(frame, textvariable=unit_of_time, width=2, font=('times, 12'))
    return sec_entry