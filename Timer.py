from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import time
from threading import Thread
import recurring_checkbox
import timer_entry
import timer_buttons
from tkinter import messagebox
from playsound import playsound

# timer_buttons.py contains style and config settings for the start and reset timer buttons

class NewTimer():
    def __init__(self, tab, tab_name):
        
        self.tab_name = tab_name
        self.tab = tab

        self.sec = StringVar()
        self.min = StringVar()
        self.hours = StringVar()
        self.recurring_on = IntVar()
        self.timer_on = False

        # create a frame for the timer
        self.new_tab_frame = ttk.Frame(self.tab, width=300, height=500)
        self.new_tab_frame.pack(fill='both', expand=True)

        # add the timer entry fields
        # config settings for the timer entry fields are found in timer_entry.py
        self.timer_frame = Frame(self.new_tab_frame)
        self.timer_frame.pack(pady=5) 


        hr_label = timer_entry.hr_label_gen(self.timer_frame)
        hr_label.pack(side=LEFT)
        hr_entry = timer_entry.hr_entry_gen(self.timer_frame, self.hours)
        hr_entry.pack(side=LEFT)

        min_label = timer_entry.min_label_gen(self.timer_frame)
        min_label.pack(side=LEFT)
        min_entry = timer_entry.min_entry_gen(self.timer_frame, self.min)
        min_entry.pack(side=LEFT)

        sec_label = timer_entry.sec_label_gen(self.timer_frame)
        sec_label.pack(side=LEFT)
        sec_entry = timer_entry.sec_entry_gen(self.timer_frame, self.sec)
        sec_entry.pack(side=LEFT)

        self.sec.set('00')
        self.min.set('00')
        self.hours.set('00')

        # add the checkbox to make the timer reset automatically
        # config settings for recurring checkbox are found in recurring_checkbox.py
        self.recurring_check = Frame(self.new_tab_frame)
        self.recurring_check.pack(pady=5)
        self.make_recurring_checkbox = recurring_checkbox.make_recurring_checkbox_gen(self.recurring_check, self.recurring_on)
        self.make_recurring_checkbox.pack()
    
        # create the start and reset timer buttons
        # config settings for timer buttons are found in timer_buttons.py
        self.button_frame = Frame(self.new_tab_frame)
        self.button_frame.pack(pady=5)

        self.start_timer = timer_buttons.start_timer_gen(self.button_frame, self.start_timer_func)
        self.start_timer.pack(fill=BOTH, expand=True, side=LEFT)

        self.reset_timer = timer_buttons.reset_timer_gen(self.button_frame, self.reset_timer_func)
        self.reset_timer.pack(fill=BOTH, expand=True, side=LEFT)

        # self.tab.mainloop()

    def countdowntimer(self):
        init_sec = int(self.sec.get())
        init_min = int(self.min.get())
        init_hours = int(self.hours.get())
        times = int(self.hours.get())*3600+ int(self.min.get())*60 + int(self.sec.get())
        while times > -1:
            if self.timer_on != True:
                break
            minute,second = (times // 60 , times % 60)
            hour =0
            if minute > 60:
                hour , minute = (minute // 60 , minute % 60)
            self.sec.set(second)
            self.min.set(minute)
            self.hours.set(hour)
            #Update the time
            self.new_tab_frame.update()
            time.sleep(1)
            if(times == 0):
                self.alarm()
                if self.recurring_on.get() == 1:
                    self.sec.set(init_sec)
                    self.min.set(init_min)
                    self.hours.set(init_hours)
                    self.countdowntimer()
                self.sec.set('00')
                self.min.set('00')
                self.hours.set('00')
                # messagebox.showinfo('Alert', f'{self.tab_name}')
            times -= 1
    
    def start_timer_func(self):
        self.timer_on = True
        timer_start = Thread(target=self.countdowntimer)
        timer_start.start()
    
    def reset_timer_func(self):
        self.timer_on = False
        self.sec.set('00')
        self.min.set('00')
        self.hours.set('00')
    
    def alarm(self):
        playsound(u'E:\Programming\\todo_list\\alarm_sound_1.mp3')
        

if __name__ == '__main__':
    NewTimer('test')