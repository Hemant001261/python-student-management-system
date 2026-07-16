from tkinter import *

def click(value):
    e.insert(END, value)

def clear():
    e.delete(0, END)

def equal():
    result = eval(e.get())
    e.delete(0, END)
    e.insert(0, result)

root = Tk()
root.title("Calculator")

e = Entry(root, width=30)
e.grid(row=0, column=0, columnspan=4)

Button(root, text="1", command=lambda: click("1")).grid(row=1,column=0)
Button(root, text="2", command=lambda: click("2")).grid(row=1,column=1)
Button(root, text="3", command=lambda: click("3")).grid(row=1,column=2)
Button(root, text="+", command=lambda: click("+")).grid(row=1,column=3)

Button(root, text="=", command=equal).grid(row=2,column=3)
Button(root, text="C", command=clear).grid(row=2,column=0)

root.mainloop()
