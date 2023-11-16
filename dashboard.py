import tkinter as tk
from game import ArithmeticGame
from admin_dashboard import AdminDashboard  # Import the AdminDashboard class

class Dashboard:
    def __init__(self, master, user_data):
        self.master = master
        self.master.title("User Dashboard")

        # Create dashboard widgets
        if isinstance(user_data, dict):
            self.welcome_label = tk.Label(master, text=f"Welcome, {user_data.get('first_name', 'User')}!", font=("Arial", 18))
            self.welcome_label.pack(pady=20)

            self.user_info_label = tk.Label(master, text=f"Email: {user_data.get('email', 'N/A')}", font=("Arial", 14))
            self.user_info_label.pack(pady=10)
            if user_data.get('role') == 'admin':
                self.admin_button = tk.Button(master, text="Admin Dashboard", command=self.open_admin_dashboard)
                self.admin_button.pack(pady=10)
            self.game_button = tk.Button(master, text="Start Game", command=self.start_game_and_close_dashboard)
            self.game_button.pack(pady=10)
            # Display other user information based on your format
            for key, value in user_data.items():
                # Skip '_id' field and password
                if key != "_id" and not key.startswith("password_"):
                    label_text = key.replace("_", " ").capitalize()
                    info_label = tk.Label(master, text=f"{label_text}: {value}", font=("Arial", 14))
                    info_label.pack(pady=5)

            self.logout_button = tk.Button(master, text="Logout", command=self.logout)
            self.logout_button.pack(pady=10)
        else:
            print("User data is not a dictionary.")

    def logout(self):
        # Add any logout functionality here
        self.master.destroy()  # Close the dashboard window

    def start_game_and_close_dashboard(self):
        # Close the dashboard
        self.master.destroy()

        # Start the game from game.py
        arithmetic_game = ArithmeticGame()
        arithmetic_game.start_game()

    def start_game(self):
        # Start the game from game.py
        game_window = tk.Toplevel(self.master)
        game_window.title("Arithmetic Game")

        arithmetic_game = ArithmeticGame()
        arithmetic_game.start_game()
    def open_admin_dashboard(self):
        # Close the current dashboard
        self.master.destroy()

        # Open the admin dashboard
        root = tk.Tk()
        admin_dashboard = AdminDashboard(root)
        root.mainloop()
# Example usage
if __name__ == '__main__':
    # Example user data
    sample_user_data = {
        "_id": {"$oid": "6556093c2cb5532537e4a20f"},
        "first_name": "2",
        "last_name": "2",
        "email": "2",
        "gender": "Male",
        "password_": "2",
        "role": "regular",
        "level": "N"
    }

    root = tk.Tk()
    dashboard = Dashboard(root, sample_user_data)
    root.mainloop()
