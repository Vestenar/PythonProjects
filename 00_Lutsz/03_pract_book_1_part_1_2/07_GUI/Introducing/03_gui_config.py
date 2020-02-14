from tkinter import *

root = Tk()
widget = Label(root)
color = 'red'
widget.config(fg=color, text="Hello world!")
widget.pack(side=LEFT, expand=YES, fill=BOTH)
root.title('gui configuration')
root.mainloop()
