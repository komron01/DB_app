import pymongo
import tkinter as tk
from tkinter import messagebox
from time import sleep

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["users"]
users_cred = {x['email']: x['password_'] for x in mycol.find()}

def login():
    def validate_login():
        username = username_var.get()
        password = password_var.get()

        if username in users_cred and users_cred[username] == password:
            result_label.config(text="Login successful!", fg="green")
            tkWindow.destroy()  # Close the login window
            tkWindow.login_status = True  # Set login status to True
        else:
            result_label.config(text="Invalid login or password", fg="red")
            tkWindow.login_status = False  # Set login status to False

    tkWindow = tk.Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('Tkinter Login Form')
    tkWindow.login_status = None  # Initialize login status

    username_label = tk.Label(tkWindow, text="User Name")
    username_label.grid(row=0, column=0)
    username_var = tk.StringVar()
    username_entry = tk.Entry(tkWindow, textvariable=username_var)
    username_entry.grid(row=0, column=1)

    password_label = tk.Label(tkWindow, text="Password")
    password_label.grid(row=1, column=0)
    password_var = tk.StringVar()
    password_entry = tk.Entry(tkWindow, textvariable=password_var, show='*')
    password_entry.grid(row=1, column=1)

    login_button = tk.Button(tkWindow, text="Login", command=validate_login)
    login_button.grid(row=2, column=0, columnspan=2)

    result_label = tk.Label(tkWindow, text="", font=("Arial", 12))
    result_label.grid(row=3, column=0, columnspan=2)

    tkWindow.mainloop()

    return tkWindow.login_status  # Return the login status after the Tkinter main loop has ended

if __name__ == '__main__':
    is_authorized = autho.login()
    if is_authorized:
        print("User is authorized.")
    else:
        print("User is not authorized.")
