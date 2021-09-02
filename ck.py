import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("300x300")
win.title("Simple Window")

frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

rb = Button(frame,text="red",fg="white",bg="red")
rb.pack(side=LEFT)
gb = Button(frame,text="green",fg="white",bg="green")
gb.pack(side=LEFT)
blb = Button(frame,text="black",fg="white",bg="black")
blb.pack(side=LEFT)
bb = Button(frame2,text="blue",fg="white",bg="blue")
bb.pack(side=BOTTOM)

lb = Listbox(frame2)
lb.insert(1,'python')
lb.insert(2,'programming')
lb.insert(3,'language')
lb.pack()

def message():
    messagebox.showinfo('From My Computer','Are You Feeling Well')

butt = Button(frame2,text="Click Me",command=message)
butt.pack()

win.mainloop()
