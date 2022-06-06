import imp
from tkinter import *
from tkinter import ttk
from complex_widgets import *
import sqlite3 as dtb


#connecting to the database
database = dtb.connect('database_users')
cursor = database.cursor()

cursor.execute('''
         CREATE TABLE IF NOT EXISTS projects (
            user_name integer PRIMARY KEY,
            name text NOT NULL,
            company text,
            email text,
            phone
          );
          ''')
                     

  
profileScreen = Tk()

input_name = InputData(profileScreen, title="name",optional=False)
input_name.pack()

input_company = InputData(profileScreen, title="company")
input_company.pack()

input_email = InputData(profileScreen, title="email")
input_email.pack()

input_telephone = InputData(profileScreen, title="telephone")
input_telephone.pack()

profileScreen.mainloop()

database.commit()
database.close()