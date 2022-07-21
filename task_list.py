from tkinter import *

#task_list.py houses the listbox settings for todo_list.py

def task_list_gen(frame):

    task_list = Listbox(
        frame,
        width=22,
        height=8,
        bd=0,
        foreground='#464646',
        highlightthickness=0,
        selectbackground = '#a6a6a6',
        activestyle='none',
        font=('Times', 18)
    )
    return task_list

def task_entry_gen(frame):
    task_entry = Entry(
        frame,
        font=('times', 14)
        )
    return task_entry