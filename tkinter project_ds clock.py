from tkinter import *
from tkinter.ttk import *
from time import strftime

root =Tk()
root.title("my digital clock")
label=Label(root, font=("ds digital" ,80), background="black", foreground="gray")
label.pack(anchor="center")

def time():
    string_1=strftime("%H: %M: %S: %p")
    label.config(text=string_1)
    label.after(1000,time)
time()

root.mainloop()
