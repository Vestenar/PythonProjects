import sys
from tkinter import *
import time

def quit():
    for i in range(5):
        print('Shutting down' + '.'*i)
        time.sleep(0.5)
    sys.exit()

widget = Button(None, text='Print and Quit', command=quit)
widget.pack()
widget.mainloop()
