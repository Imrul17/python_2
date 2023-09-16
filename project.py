from tkinter import *
root=Tk()
root.title("my calculator")
# Entry section
entry=Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10,pady=10)
entry.focus_set()
#funtion area
def buttonclick(number):
    currentclick=entry.get()
    entry.delete(0, END)
    entry.insert(0, str(currentclick)+str (number))

def button_clear():
    entry.delete(0, END)
def button_add():
    first_number=entry.get()
    global n_number
    n_number=int(first_number)
    entry.delete(0,END)

def button_equal():
    sec_number=entry.get()
    entry.delete(0,END)
    entry.insert(0, int(n_number)+int(sec_number))

#button section
button_1=Button(root, text="1",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(1))
button_2=Button(root, text="2",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(2))
button_3=Button(root, text="3",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(3))
button_sub=Button(root, text="-",padx=30,pady=15,background="black",foreground="red",command=buttonclick)

button_4=Button(root, text="4",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(4))
button_5=Button(root, text="5",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(5))
button_6=Button(root, text="6",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(6))
button_mul=Button(root, text="*",padx=30,pady=15,background="black",foreground="red",command=buttonclick)

button_7=Button(root, text="7",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(7))
button_8=Button(root, text="8",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(8))
button_9=Button(root, text="9",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(9))
button_div=Button(root, text="/",padx=30,pady=15,background="black",foreground="red",command=buttonclick)

button_0=Button(root, text="0",padx=30,pady=15,background="black",foreground="red",command=lambda:buttonclick(0))
button_clear=Button(root, text="C",padx=30,pady=15,background="black",foreground="red",command=button_clear)
button_equal=Button(root, text="=",padx=30,pady=15,background="black",foreground="red",command=button_equal)
button_add=Button(root, text="+",padx=30,pady=15,background="black",foreground="red",command=button_add)

button_1.grid(row=3,column=0,)
button_2.grid(row=3,column=1,)
button_3.grid(row=3,column=2,)
button_sub.grid(row=3,column=3,)

button_4.grid(row=2,column=0,)
button_5.grid(row=2,column=1,)
button_6.grid(row=2,column=2,)
button_mul.grid(row=2,column=3,)

button_7.grid(row=1,column=0,)
button_8.grid(row=1,column=1,)
button_9.grid(row=1,column=2,)
button_div.grid(row=1,column=3,)

button_0.grid(row=4,column=0,)
button_clear.grid(row=4,column=1,)
button_equal.grid(row=4,column=2,)
button_add.grid(row=4,column=3,)



root.mainloop()
