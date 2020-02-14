import sys
from tkinter import mainloop, Button

x = Button(
    text="Press me",
    command=(lambda: sys.stdout.write("Spam\n")))
x.pack()
mainloop()