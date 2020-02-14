from tkinter import *
from guicontainer import MyFrame

class HelloExtender(MyFrame):

    def make_widgets(self):
        MyFrame.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('hello', self.data)
        # MyFrame.message(self)


if __name__ == '__main__':
    HelloExtender().mainloop()