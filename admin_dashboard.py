import tkinter as tk
from tkinter import ttk
import pymongo

class AdminDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Dashboard")

        # MongoDB connection
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["admin"]
        mycol = mydb["users"]

        # Get the list of users from the database
        user_list = list(mycol.find())

        # Create a treeview to display the user list
        self.tree = ttk.Treeview(master, columns=('First Name', 'Last Name', 'Email', 'Gender', 'Role', 'Level'))
        self.tree.heading('#0', text='ID')  # ID column

        # Insert user data into the treeview
        for user in user_list:
            user_id = str(user.get('_id', 'N/A'))
            self.tree.insert('', 'end', iid=user_id, text=user_id, values=(user.get('first_name', 'N/A'),
                                                                           user.get('last_name', 'N/A'),
                                                                           user.get('email', 'N/A'),
                                                                           user.get('gender', 'N/A'),
                                                                           user.get('role', 'N/A'),
                                                                           user.get('level', 'N/A')))

        # Set column names for treeview
        column_names = ['First Name', 'Last Name', 'Email', 'Gender', 'Role', 'Level']
        for i, name in enumerate(column_names):
            self.tree.heading(f'#{i+1}', text=name)

        self.tree.pack(padx=10, pady=10)

        # Create a button to close the admin dashboard
        self.close_button = tk.Button(master, text="Close", command=self.close_admin_dashboard)
        self.close_button.pack(pady=10)

    def close_admin_dashboard(self):
        # Close the admin dashboard window
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    admin_dashboard = AdminDashboard(root)
    root.mainloop()
