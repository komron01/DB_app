import tkinter as tk
from tkinter import messagebox
import pymongo

def register_user():
    first_name = first_name_var.get()
    last_name = last_name_var.get()
    email = email_var.get()
    gender = gender_var.get()
    password = password_var.get()

    # Validate that all fields are filled
    if not all([first_name, last_name, email, gender, password]):
        messagebox.showerror("Error", "All fields are required.")
        return

    # MongoDB connection
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["admin"]
    mycol = mydb["users"]

    # Check if the email already exists
    if mycol.find_one({"email": email}):
        messagebox.showerror("Error", "Email already exists. Please use a different email.")
        return

    # Insert new user into the database with role "regular"
    new_user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "gender": gender,
        "password_": password,
        "role": "regular",
        "level": "N"
    }

    mycol.insert_one(new_user)
    messagebox.showinfo("Success", "User registered successfully!")

    # Clear the form
    clear_form()
    root.destroy()

def clear_form():
    first_name_var.set("")
    last_name_var.set("")
    email_var.set("")
    gender_var.set("")
    password_var.set("")

# Create the main window
root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x250")

# Variables for storing user input
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_var = tk.StringVar()
gender_var = tk.StringVar()
password_var = tk.StringVar()

# Labels and Entry widgets for the registration form
tk.Label(root, text="First Name:").grid(row=0, column=0)
tk.Entry(root, textvariable=first_name_var).grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0)
tk.Entry(root, textvariable=last_name_var).grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
tk.Entry(root, textvariable=email_var).grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
# Use a dropdown menu for gender
gender_options = ["Male", "Female"]
tk.OptionMenu(root, gender_var, *gender_options).grid(row=3, column=1)

tk.Label(root, text="Password:").grid(row=4, column=0)
tk.Entry(root, textvariable=password_var, show='*').grid(row=4, column=1)

# Register button
tk.Button(root, text="Register", command=register_user).grid(row=5, column=0, columnspan=2)

# Clear button
tk.Button(root, text="Clear", command=clear_form).grid(row=6, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
