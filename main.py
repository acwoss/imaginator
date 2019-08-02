import tkinter
from imaginator import Imaginator

__version__ = '0.1.0'

app = tkinter.Tk()
app.title(f'Imaginator {__version__} - Tuning Parts')
app.resizable(False, False)

imaginator = Imaginator(app)

app.mainloop()
