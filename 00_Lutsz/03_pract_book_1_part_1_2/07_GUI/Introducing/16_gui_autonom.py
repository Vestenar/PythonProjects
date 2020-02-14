from tkinter import *
from guiautonom import HelloPackage

frm = Frame()
frm.pack()
Label(frm, text='hello').pack()

part = HelloPackage(frm)
part.top.pack(side=RIGHT)
frm.mainloop()
