from tkinter import Frame, Button

class MyFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Hello frame', command=self.message)
        widget.pack(side='left')

    def message(self):
        self.data += 1
        print(f'Hello frame {self.data}')
        if self.data >= 45:
            self.quit()


if __name__ == '__main__':
    MyFrame().mainloop()