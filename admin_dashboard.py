import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pymongo
from bson import ObjectId


class AdminDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Dashboard")

        # MongoDB connection
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["admin"]
        self.mycol = mydb["users"]

        # Get the list of users from the database
        user_list = list(self.mycol.find())

        # Create a treeview to display the user list
        self.tree = ttk.Treeview(master, columns=('ID', 'First Name', 'Last Name', 'Email', 'Gender', 'Role', 'Level'))
        self.tree.heading('#0', text='ID')  # ID column

        # Insert user data into the treeview
        for user in user_list:
            user_id = str(user.get('_id', 'N/A'))
            self.tree.insert('', 'end', text=user_id, values=(user.get('first_name', 'N/A'),
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

        # Create buttons for actions
        self.delete_button = tk.Button(master, text="Delete User", command=self.delete_user)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(master, text="Edit User", command=self.edit_user)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.reset_password_button = tk.Button(master, text="Reset Password", command=self.reset_password)
        self.reset_password_button.pack(pady=10)

       

        self.close_button = tk.Button(master, text="Close", command=self.close_admin_dashboard)
        self.close_button.pack(side=tk.RIGHT, padx=5)

    def delete_user(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = selected_item[0]
            confirmation = simpledialog.askstring("Delete User", "Are you sure you want to delete this user? (yes/no)")
            if confirmation.lower() == 'yes':
                self.mycol.delete_one({'_id': ObjectId(user_id)})
                self.tree.delete(user_id)
        else:
            messagebox.showinfo("Error", "Please select a user to delete.")

    def edit_user(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = selected_item[0]
            user_data = self.mycol.find_one({'_id': ObjectId(user_id)})
            if user_data:
                # Get the current values of first_name and last_name
                current_first_name = user_data.get('first_name', '')
                current_last_name = user_data.get('last_name', '')

                # Prompt the user for new values using simpledialog
                new_first_name = simpledialog.askstring("Edit User", "Enter new first name:", initialvalue=current_first_name)
                new_last_name = simpledialog.askstring("Edit User", "Enter new last name:", initialvalue=current_last_name)
                # ... Repeat for other fields

                # Update the user data in the database
                self.mycol.update_one({'_id': ObjectId(user_id)}, {'$set': {'first_name': new_first_name, 'last_name': new_last_name}})
                
                # Refresh the treeview with the updated data
                self.refresh_treeview()

            else:
                messagebox.showinfo("Error", "User not found.")
        else:
            messagebox.showinfo("Error", "Please select a user to edit.")

    def refresh_treeview(self):
        # Refresh the treeview with updated user data
        self.tree.delete(*self.tree.get_children())
        user_list = list(self.mycol.find())
        for user in user_list:
            user_id = str(user.get('_id', 'N/A'))
            self.tree.insert('', 'end', iid=user_id, text=user_id, values=(user.get('first_name', 'N/A'),
                                                                           user.get('last_name', 'N/A'),
                                                                           user.get('email', 'N/A'),
                                                                           user.get('gender', 'N/A'),
                                                                           user.get('role', 'N/A'),
                                                                           user.get('level', 'N/A')))

    def reset_password(self):
        # Prompt the user to select a user for password reset
        selected_item = self.tree.selection()
        if selected_item:
            user_id = selected_item[0]
            user_data = self.mycol.find_one({'_id': ObjectId(user_id)})
            if user_data:
                # Prompt the user for a new password using simpledialog
                new_password = simpledialog.askstring("Reset Password", "Enter new password:")
                # ... Validate and set the new password (you might want to hash it)

                # Update the user's password in the database
                self.mycol.update_one({'_id': ObjectId(user_id)}, {'$set': {'password_': new_password}})
                
                # Inform the user that the password has been reset
                messagebox.showinfo("Password Reset", "Password reset successfully.")
            else:
                messagebox.showinfo("Error", "User not found.")
        else:
            messagebox.showinfo("Error", "Please select a user to reset the password.")
 
    def close_admin_dashboard(self):
        # Close the admin dashboard window
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    admin_dashboard = AdminDashboard(root)
    root.mainloop()
