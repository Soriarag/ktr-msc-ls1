import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import sqlite3 as dtb
from complex_widgets import *

database = dtb.connect('database_users')

global cursor

cursor = database.cursor()

cursor.execute('''
         CREATE TABLE IF NOT EXISTS user_profiles (
            user_name text PRIMARY KEY,
            name text NOT NULL,
            company text,
            email text,
            phone text
          );
          ''')

cursor.execute('''
         CREATE TABLE IF NOT EXISTS user_data (
            user_name text PRIMARY KEY,
            password text NOT NULL,
          );
          ''')

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, SignUp, Profile):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.input_user = InputData(self, title="user name", optional=False)
        self.input_user.pack()
        
        self.input_password = InputData(self, title="password", optional=False)
        self.input_password.pack()
       
        login = tk.Button(self, text="Login",
                            command=self.check_login)
        login.pack()
        
        sign_up = tk.Button(self, text="Sign up instead",
                            command=lambda: controller.show_frame("SignUp"))
        sign_up.pack()
        
    def check_login(self):
      
      typed_user = self.input_user.get_input()
      typed_password = self.input_password.get_input()
      global cursor
      cursor.execute("SELECT * FROM user_data WHERE user_name = " + typed_user + " AND password = " + typed_password)
      if cursor.fetchall().count() == 0:
        print("user does not exist")
      else:
        print("user does exist")


class Profile(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="profile", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        input_name = InputData(self, title="name", optional=False)
        input_name.pack()

        input_company = InputData(self, title="company")
        input_company.pack()

        input_email = InputData(self, title="email")
        input_email.pack()

        input_telephone = InputData(self, title="telephone")
        input_telephone.pack()

        save_info = ButtonSaveInputs(self, cursor, "default_user", [
                                    input_name, input_company, input_email, input_telephone])
        save_info.pack()



class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.input_user = InputData(self, title="user name", optional=False)
        self.input_user.pack()
        
        self.input_password = InputData(self, title="password", optional=False)
        self.input_password.pack()
       
        sign_up = tk.Button(self, text="Sign up",
                            command=self.add_user)
        sign_up.pack()
        
        login = tk.Button(self, text="login instead",
                            command=lambda: controller.show_frame("SignUp"))
        login.pack()
        
    def add_user(self):
      
      typed_user = self.input_user.get_input()
      typed_password = self.input_password.get_input()
      global cursor
      cursor.execute("SELECT * FROM user_data WHERE user_name = " + typed_user)
      if cursor.fetchall().count() == 0:
        Label(self.controller, text="user exists")
      else:
        cursor.execute("INSERT into user_data VALUES(" + typed_user + "," + typed_password + ")")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    database.commit()
    database.close()