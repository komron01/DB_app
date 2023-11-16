import tkinter as tk
from autho import login
from dashboard import Dashboard
from game import ArithmeticGame

if __name__ == '__main__':
    user_data = login()

    if user_data is not None and user_data is not False:
        print("User is authorized.")
        root = tk.Tk()
        dashboard = Dashboard(root, user_data)
        root.mainloop()
    else:
        print("User is not authorized.")
