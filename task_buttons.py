from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

# task_buttons.py contains the style and config settings for the add and delete task buttons

def add_task_style_gen():
    add_task_style = ttk.Style()

    add_task_style.configure(
        'Add_Task.TButton',
        background='green2',
        font=('times 14'),
        padx=20,
        pady=10,
        relief='raised',
        bordercolor='green2'
    )
    return 'Add_Task.TButton'

def addTask_btn_gen(frame, cmd):
    addTask_btn = Button(
        frame,
        text='Add Task',
        command=cmd,
        style=add_task_style_gen()
    )
    return addTask_btn

def del_task_style_gen():
    del_task_style = ttk.Style()

    del_task_style.configure(
        'Del_Task.TButton',
        background='red',
        font=('times 14'),
        padx=20,
        pady=10
    )
    return 'Del_Task.TButton'

def delTask_btn_gen(frame, cmd):
    delTask_btn = Button(
        frame,
        text='Delete Task',
        command=cmd,
        style=del_task_style_gen()
    )
    return delTask_btn