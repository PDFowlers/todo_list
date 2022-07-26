import task_list
import task_buttons
import timer_entry
import recurring_checkbox
import timer_buttons
import Timer
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
import time
from threading import Thread



# todo_list.py will launch an application that can be used as a to-do list
# the application will store tasks or items to remember, sorted by priority, and have alarms to remind the user of certain tasks

# newTask and deleteTask are the fucntions called when pressing the Add and Delete task buttons respectively

def newTask():
    task = task_entry.get()
    if task != "":
        task_list_widget.insert(END, task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    task_list_widget.delete(ANCHOR)

def add_timer_func():
    if task_list_widget.get(ANCHOR) != '':
        new_tab_frame = ttk.Frame(todo_list_notebook, width=300, height=500)
        new_tab_frame.pack(fill='both', expand=True)

        todo_list_notebook.add(new_tab_frame, text=task_list_widget.get(ANCHOR))
        tab_name = task_list_widget.get(ANCHOR)

        Timer.NewTimer(new_tab_frame, tab_name)
    
    else:
        messagebox.showwarning("warning", "Please select a task.")

# initial Tk instance setup
root = Tk()
root.geometry('300x500+0+0')
root.title('To Do List')
root.config(bg = 'DeepSkyBlue')
root.resizable(width=True, height=True)

# first notebook tab creation

todo_tab_style = Style()
todo_tab_style.configure('Todo.TNotebook', background='DeepSkyBlue', foreground='DeepSkyBlue', font=('times, 12'))
todo_list_notebook = Notebook(root, style='Todo.TNotebook')
todo_list_notebook.pack(pady=5)

todo = Frame(todo_list_notebook, width=300, height=500, style='Todo.Tab')
todo.pack(fill='both', expand=True)

todo_list_notebook.add(todo, text='To-Do List')

# task list + scrollbar palcement. 
# task list and task entry settings can be found in task_list.py

task_list_frame = Frame(todo)
task_list_frame.pack(pady=10)

task_list_widget = task_list.task_list_gen(task_list_frame)
task_list_widget.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(task_list_frame)
sb.pack(side=RIGHT, fill=BOTH)
task_list_widget.config(yscrollcommand=sb.set)
sb.config(command=task_list_widget.yview)

task_entry = task_list.task_entry_gen(todo)
task_entry.pack(pady=5)

# add and delete task buttons to call their respctive functions on tasks in the entry area or the listbox area
# add and delete task button settings can be found in task_buttons.py

button_frame = Frame(todo)
button_frame.pack(pady=5)

addTask_btn = task_buttons.addTask_btn_gen(button_frame, newTask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = task_buttons.delTask_btn_gen(button_frame, deleteTask)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# add timer button

add_timer_frame = Frame(todo)
add_timer_frame.pack(pady=5)

add_timer_button = timer_buttons.add_timer_gen(add_timer_frame, add_timer_func)
add_timer_button.pack(fill=BOTH, expand=True, side=LEFT)

if __name__ == '__main__':
    todo.mainloop()