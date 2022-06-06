from tkinter import *
from tkinter import ttk
import sqlite3 as dtb


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
    
  def get_input(self):
    return self.entry.get()


class ButtonSaveInputs:
  
  def __init__(self, screen, user:str, inputs = [InputData]):
    self.inputs = inputs
    self.user = user
    self.button = Button(screen, text="Save", command=self.save)
    
  def save(self):
    for input_box in self.inputs:
      input_box.get_input()
  