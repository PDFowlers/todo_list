from tkinter import *
from tkinter import messagebox

# todo_list.py will launch an application that can be used as a to-do list
# the application will store tasks or items to remember, sorted by priority, and have alarms to remind the user of certain tasks

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task + str(timer_on.get()))
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)


todo = Tk()
todo.geometry('300x500+0+0')
todo.title('To Do List')
todo.config(bg = 'DeepSkyBlue')
todo.resizable(width=True, height=True)

frame = Frame(todo)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=23,
    height=12,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    todo,
    font=('times', 14)
    )

my_entry.pack(pady=5)

button_frame = Frame(todo)
button_frame.pack(pady=5)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)



todo.mainloop()