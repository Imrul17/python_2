#button section

from tkinter import *
root=Tk()
def mybtn():
    mybutton=Label(root, text="hello world")
    mybutton.grid(row=1, column=0)
button=Button(root, text="click me",bg="gray",fg="red", padx=10,pady=10, command=mybtn)
button.grid(row=0, column=0)
root.mainloop()