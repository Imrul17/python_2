from tkinter import*
root=Tk()

entry =Entry(root, width=50,bg="green",fg="black",borderwidth=30)
entry.focus_set()
entry.grid(row=0,column=0)

def mybtn():
    botton =entry.get()
    label =Label(root, text=botton)
    label.grid(row=2, column=0)

botton=Button(root, text="click me",pady=10,padx=10, command=mybtn)
botton.grid(row=1, column=0)
root.mainloop()