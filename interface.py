from tkinter import *
from tkinter import ttk

class InputData:
  def __init__(self, screen, title="", optional=True) -> None:
    if (optional):
      title += " (optional)"
    else:
      title += " (mandatory)"
    self.title = Label(screen, text=title)
    self.entry = Entry(screen)
    
  def pack(self):
    self.title.pack()
    self.entry.pack()
  
  
mainScreen = Tk()

input_name = InputData(mainScreen, title="name",optional=False)
input_name.pack()

input_company = InputData(mainScreen, title="company")
input_company.pack()

input_email = InputData(mainScreen, title="email")
input_email.pack()

input_telephone = InputData(mainScreen, title="telephone")
input_telephone.pack()

mainScreen.mainloop()
