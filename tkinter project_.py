from tkinter import*
root=Tk()

entry =Entry(root, width=50,bg="green",fg="black",borderwidth=30)
entry.focus_set()
entry.insert(0, 'enter your name : ')
entry.grid(row=0,column=0)

def myclick():
    botton =entry.get()
    label=Label(root, text=botton)
    label.grid(row=3, column=0)

button=Button(root, text="click me", padx=10,pady=10, command = myclick)
button.grid(row=1,column=0)

root.mainloop()