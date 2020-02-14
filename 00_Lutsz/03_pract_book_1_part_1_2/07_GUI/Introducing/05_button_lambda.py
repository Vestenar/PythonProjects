import sys
from tkinter import *

widget = Button(None,
                text='Press me!',                                           # lambda-выражения могут содержать только одно выражение, поэтому здесь
                command=lambda: print('Shutting down') or sys.exit())       # используется оператор or, чтобы заставить выполниться два выражения
widget.pack()
widget.mainloop()
