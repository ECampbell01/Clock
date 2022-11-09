from tkinter import *
from time import *

def update():
    clock_time = strftime("%I:%M:%S %p")
    time_label.config(text = clock_time)

    clock_day = strftime("%A")
    day_label.config(text=clock_day)

    clock_date = strftime("%B %d, %Y")
    date_label.config(text=clock_date)

    window.after(1000, update)

window = Tk()
window.title("Clock")
window.geometry("450x200")
window.config(background = "black")

time_label = Label(window, font = ("Arial", 50), fg = "red", bg = "black")
time_label.pack()

day_label = Label(window, font = ("Arial", 25), fg = "green", bg = "black")
day_label.pack()

date_label = Label(window, font = ("Arial", 30), fg = "white", bg = "black")
date_label.pack()

update()

window.mainloop()