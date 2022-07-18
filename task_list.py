from tkinter import *

#task_list.py houses the listbox settings for todo_list.py
frame=Frame()
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

if __name__ == '__main__':
    todo.mainloop()