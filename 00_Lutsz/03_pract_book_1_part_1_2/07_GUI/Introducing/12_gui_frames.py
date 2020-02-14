from sys import exit
from tkinter import *
from guicontainer import MyFrame

parent = Frame(None)
parent.pack()
Myframe(parent).pack(side=RIGHT)

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
