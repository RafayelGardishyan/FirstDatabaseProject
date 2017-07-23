import sqlite3
from tkinter import *
import tkinter.messagebox
import re

stop = False
dbname = 'MyFirstSQLApp'

class GUI:
    def __init__(self):
        self.root = Tk()
        self.window = Frame(self.root)
        self.labName = Label(self.window, text="Name:", bd=5)
        self.entName = Entry(self.window, width=25, bd=5)
        self.labPhone = Label(self.window, text="Phone:", bd=5)
        self.entPhone = Entry(self.window, width=25, bd=5)
        self.labEmail = Label(self.window, text="Email:", bd=5)
        self.entEmail = Entry(self.window, width=25, bd=5)
        self.labPassword = Label(self.window, text="Password:", bd=5)
        self.entPassword = Entry(self.window, width=25, show="*", bd=5)
        self.submitbtn = Button(self.window, text="Submit", width="30", bd=5)

        self.window.grid(row=0, column=0, ipadx=5, ipady=5, pady=5, padx=5)
        self.labName.grid(row=0, column=0)
        self.entName.grid(row=0, column=1)
        self.labPhone.grid(row=1, column=0)
        self.entPhone.grid(row=1, column=1)
        self.labEmail.grid(row=2, column=0)
        self.entEmail.grid(row=2, column=1)
        self.labPassword.grid(row=3, column=0)
        self.entPassword.grid(row=3, column=1)
        self.submitbtn.grid(row=4, column=0, columnspan=2)

        self.submitbtn.bind("<Button-1>", self.insert)

        self.root.title("Add User")
        self.root.mainloop()

    def insert(self, event):
        self.name = self.entName.get()
        self.phone = self.entPhone.get()
        self.email = self.entEmail.get()
        self.password = self.entPassword.get()
        self.db = sqlite3.connect(dbname)
        print("Connected successfully")
        self.cursor = self.db.cursor()

        if len(self.name) != 0:
            if len(self.phone)!= 0:
                if len(self.email) != 0:
                    if len(self.password) != 0:
                        if re.match("[^@]+@[^@]+\.[^@]+", self.email):
                            try:
                                self.cursor.execute('''INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?) ''',
                                                    (self.name, self.phone, self.email, self.password))
                                print("User Inserted")
                                tkinter.messagebox.showinfo("Success", "User successfully added!")

                            except sqlite3.IntegrityError:
                                print("Email already exists")
                                tkinter.messagebox.showwarning("Error", "An account with this email already exists!")
                                stop = True

                        else:
                            tkinter.messagebox.showwarning("Warning", "You have to enter a valid email address!")
                    else:
                        tkinter.messagebox.showwarning("Warning", "You have to fill all the fields!")
                else:
                    tkinter.messagebox.showwarning("Warning", "You have to fill all the fields!")
            else:
                tkinter.messagebox.showwarning("Warning", "You have to fill all the fields!")
        else:
            tkinter.messagebox.showwarning("Warning", "You have to fill all the fields!")

        self.db.commit()
        self.cursor.execute("SELECT id, name FROM users ORDER BY id")
        self.results = self.cursor.fetchall()
        print(self.results)

class dbConnect:
    def __init__(self):
        self.db = sqlite3.connect(dbname)
        print("Connected successfully")
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY , name TEXT, phone TEXT, email TEXT UNIQUE, password TEXT)''')
            print("Created table successfully")
        except sqlite3.OperationalError:
            print("Table exists")
        self.db.commit()
        self.db.close()



obj = dbConnect()
window = GUI()

obj.db.close()
print("Databse Closed")
