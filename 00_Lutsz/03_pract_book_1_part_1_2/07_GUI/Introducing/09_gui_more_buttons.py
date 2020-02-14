from tkinter import *


def greeting():
    print('hello')


win = Frame()
win.pack()

Label(win, text='Press any button').pack(side=TOP)
Button(win, text='Greet', command=greeting).pack(side=LEFT)
Button(win, text='Exit', command=win.quit).pack(side=RIGHT)
win.mainloop()


