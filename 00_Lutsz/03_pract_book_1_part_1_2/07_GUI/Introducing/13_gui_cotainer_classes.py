from tkinter import *
from guicontainer import MyFrame

class HelloContainer(Frame):

    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makewidget()

    def makewidget(self):
        MyFrame(self).pack(side=RIGHT)
        Button(self, text='Attach', command=self.quit).pack(side=LEFT)

if __name__ == '__main__':
    HelloContainer().mainloop()