from optparse import Values
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
  
  def __init__(self, screen, cursor, user:str, inputs = [InputData]):
    self.inputs = inputs
    self.user = user
    self.cursor = cursor
    self.button = Button(screen, text="Save", command=self.save)
  
  def save(self):
    
    values = "VALUES ('" + self.user + "'"
    for input_box in self.inputs:
      values += ",'" + input_box.get_input()+"'"
    
    values += ");"
    
    print(values)
    
    self.cursor.execute("REPLACE INTO users " + values)
    
  def pack(self):
     self.button.pack()