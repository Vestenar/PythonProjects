from tkinter import *
import sys


class HelloClass():
    def __init__(self):
        widget = Button(None, text='Anytext', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class GUI')
        sys.exit()


HelloClass()
mainloop()
