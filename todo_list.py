from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *

# todo_list.py will launch an application that can be used as a to-do list
# the application will store tasks or items to remember, sorted by priority, and have alarms to remind the user of certain tasks

# newTask and deleteTask are the fucntions called when pressing the Add and Delete task buttons respectively

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task + str(timer_on.get()))
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

# initial Tk instance setup
todo = Tk()
todo.geometry('300x500+0+0')
todo.title('To Do List')
todo.config(bg = 'DeepSkyBlue')
todo.resizable(width=True, height=True)

frame = Frame(todo)
frame.pack(pady=10)

# listbox that will present all the tasks on the list

lb = Listbox(
    frame,
    width=22,
    height=13,
    bd=0,
    foreground='#464646',
    highlightthickness=0,
    selectbackground = '#a6a6a6',
    activestyle='none',
    font=('Times', 18)
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# task entry area
my_entry = Entry(
    todo,
    font=('times', 14)
    )

my_entry.pack(pady=5)

# this checkbox will enable the use of a timer to remind the user to complete the task
timercheck_style = ttk.Style()
timercheck_style.configure(
    'Timercheck.TCheckbutton',
    foreground='black',
    background='DeepSkyBlue'
)
timer_check = Frame(todo)
timer_check.pack(pady=5)
timer_on = IntVar()

timer_checkbox = Checkbutton(
    timer_check,
    text='Add Timer',
    variable=timer_on,
    onvalue=1,
    offvalue=0,
    style='Timercheck.TCheckbutton'
)

timer_checkbox.pack()

# add and delete task buttons to call their respctive functions on tasks in the entry area or the listbox area

button_frame = Frame(todo)
button_frame.pack(pady=5)

add_task_style = ttk.Style()
# add_task_style.theme_use('default')
add_task_style.configure(
    'Add_Task.TButton',
    background='green2',
    font=('times 14'),
    padx=20,
    pady=10,
    relief='raised',
    bordercolor='green2'
)
# add_task_style.map('Add_Task.TButton', background=[('active','green2')])
addTask_btn = Button(
    button_frame,
    text='Add Task',
    command=newTask,
    style='Add_Task.TButton'
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

del_task_style = ttk.Style()
del_task_style.configure(
    'Del_Task.TButton',
    background='red',
    font=('times 14'),
    padx=20,
    pady=10
)
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    command=deleteTask,
    style='Del_Task.TButton'
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


if __name__ == '__main__':
    todo.mainloop()