import sys
from tkinter import *

class HelloCallable():
    def __init__(self):
        self.message = 'Hello everything'

    def __call__(self):
        print(self.message)
        sys.exit()

widget = Button(None, text='Close', command=HelloCallable())
widget.pack()
mainloop()