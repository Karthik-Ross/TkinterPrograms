import tkinter
from tkinter import *

win = Tk()

s = Scale(win)
s.pack()
spb = Spinbox(win, from_ = 0, to_ = 20)
spb.pack()

scb = Scrollbar(win)
scb.pack(side=RIGHT,fill=Y)

list = Listbox(win, yscrollcommand=scb.set)

for line in range(100):
    list.insert(END,"This is line number : " + str(line))

list.pack(side=LEFT,fill=BOTH)

win.mainloop()
