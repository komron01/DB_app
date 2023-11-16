import tkinter as tk

class Dashboard:
    def __init__(self, master, user_data):
        print("User Data in Dashboard:", user_data) 
        self.master = master
        self.master.title("User Dashboard")

        # Create dashboard widgets
        if isinstance(user_data, dict):
            self.welcome_label = tk.Label(master, text=f"Welcome, {user_data.get('first_name', 'User')}!", font=("Arial", 18))
            self.welcome_label.pack(pady=20)

            self.user_info_label = tk.Label(master, text=f"Email: {user_data.get('email', 'N/A')}", font=("Arial", 14))
            self.user_info_label.pack(pady=10)

            # Display other user information based on your format
            for key, value in user_data.items():
                # Skip '_id' field
                if key != "_id"  and not key.startswith("password_"):
                    label_text = key.replace("_", " ").capitalize()
                    info_label = tk.Label(master, text=f"{label_text}: {value}", font=("Arial", 14))
                    info_label.pack(pady=5)

            self.logout_button = tk.Button(master, text="Logout", command=self.logout)
            self.logout_button.pack(pady=10)
        else:
            print("User data is not a dictionary.")
            
    def show_user_info(self):
        # This method can be expanded to display user information or perform other actions
        info_window = tk.Toplevel(self.master)
        info_window.title("User Information")

        # Example: Display some information
        info_label = tk.Label(info_window, text="User Information Goes Here", font=("Arial", 14))
        info_label.pack(pady=20)

    def logout(self):
        # Add any logout functionality here
        self.master.destroy()  # Close the dashboard window

