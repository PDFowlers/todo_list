import task_list
from cgitb import text
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
    task = my_entry.get()
    if task != "":
        task_list_widget.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    task_list_widget.delete(ANCHOR)

def countdowntimer():
    init_sec = int(sec.get())
    init_min = int(min.get())
    init_hours = int(hours.get())
    times = int(hours.get())*3600+ int(min.get())*60 + int(sec.get())
    while times > -1:
        if timer_on != True:
            break
        minute,second = (times // 60 , times % 60)
        hour =0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
        sec.set(second)
        min.set(minute)
        hours.set(hour)
        #Update the time
        todo.update()
        time.sleep(1)
        if(times == 0):
            if recurring_on.get() == 1:
                sec.set(init_sec)
                min.set(init_min)
                hours.set(init_hours)
                countdowntimer()
            sec.set('00')
            min.set('00')
            hours.set('00')
        times -= 1

def start_timer():
    global timer_on
    timer_on = True
    timer_start = Thread(target=countdowntimer)
    timer_start.start()


def reset_timer():
    global timer_on
    timer_on = False
    sec.set('00')
    min.set('00')
    hours.set('00')

# initial Tk instance setup
todo = Tk()
todo.geometry('300x500+0+0')
todo.title('To Do List')
todo.config(bg = 'DeepSkyBlue')
todo.resizable(width=True, height=True)

# task list + scrollbar palcement
task_list_frame = Frame(todo)
task_list_frame.pack(pady=10)
task_list_widget = task_list.task_list_gen(task_list_frame)
task_list_widget.pack(side=LEFT, fill=BOTH)
sb = Scrollbar(task_list_frame)
sb.pack(side=RIGHT, fill=BOTH)
task_list_widget.config(yscrollcommand=sb.set)
sb.config(command=task_list_widget.yview)

# task entry area
my_entry = Entry(
    todo,
    font=('times', 14)
    )

my_entry.pack(pady=5)

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

# creating the 3 entry fields for the timer

timer_frame = Frame(todo)
timer_frame.pack(pady=5) 

hr_label_style = Style()
hr_label_style.configure('Hr_Label.TLabel', background='DeepSkyBlue', font=('times, 12'))
hr_label = Label(timer_frame, style = 'Hr_Label.TLabel', text = 'hours')
hr_label.pack(side=LEFT)
hours = StringVar()
hr_entry = Entry(timer_frame, textvariable=hours, width=2, font=('times, 12'))
hr_entry.pack(side=LEFT)

min_label_style = Style()
min_label_style.configure('Min_Label.TLabel', background='DeepSkyBlue', font=('times, 12'))
min_label = Label(timer_frame, style='Min_Label.TLabel', text='min', background='DeepSkyBlue')
min_label.pack(side=LEFT)
min = StringVar()
min_entry = Entry(timer_frame, textvariable=min, width=2, font=('times, 12'))
min_entry.pack(side=LEFT)

sec_label_style = Style()
sec_label_style.configure('Sec_Label.TLabel', background='DeepSkyBlue', font=('times, 12'))
sec_label = Label(timer_frame, style='Sec_Label.TLabel', text='sec', background='DeepSkyBlue')
sec_label.pack(side=LEFT)
sec = StringVar()
sec_entry = Entry(timer_frame, textvariable=sec, width=2, font=('times, 12'))
sec_entry.pack(side=LEFT)

sec.set('00')
min.set('00')
hours.set('00')

# this checkbox will allow the timer to automatically reset to the start every time it ends, allowing instant re-use of the same timer
make_recurring = ttk.Style()
make_recurring.configure(
    'Recurring.TCheckbutton',
    foreground='black',
    background='DeepSkyBlue'
)
recurring_check = Frame(todo)
recurring_check.pack(pady=5)
recurring_on = IntVar()

recurring_checkbox = Checkbutton(
    recurring_check,
    text='Make Recurring',
    variable=recurring_on,
    onvalue=1,
    offvalue=0,
    style='Recurring.TCheckbutton'
)

recurring_checkbox.pack()

# start and stop buttons for the timer

button_frame = Frame(todo)
button_frame.pack(pady=5)

start_timer_style = ttk.Style()
# add_task_style.theme_use('default')
start_timer_style.configure(
    'Start.TButton',
    background='green2',
    font=('times 14'),
    padx=20,
    pady=10,
    relief='raised',
    bordercolor='green2'
)
# add_task_style.map('Add_Task.TButton', background=[('active','green2')])
start_timer = Button(
    button_frame,
    text='Start Timer',
    command=start_timer,
    style='Start.TButton'
)
start_timer.pack(fill=BOTH, expand=True, side=LEFT)

reset_timer_style = ttk.Style()
reset_timer_style.configure(
    'Reset.TButton',
    background='red',
    font=('times 14'),
    padx=20,
    pady=10
)
reset_timer = Button(
    button_frame,
    text='Reset Timer',
    command=reset_timer,
    style='Reset.TButton'
)
reset_timer.pack(fill=BOTH, expand=True, side=LEFT)

if __name__ == '__main__':
    todo.mainloop()