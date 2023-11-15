import tkinter as tk
from PIL import Image, ImageTk
import autho
import random
from tkinter import messagebox

class ArithmeticGame:
    def __init__(self):
        self.num1, self.num2 = 0, 0
        self.feedback_label = None

    def generate_question(self):
        self.num1 = random.randint(10, 1000)
        self.num2 = random.randint(10, 1000)

    def check_answer(self):
        user_answer = self.entry.get()

        try:
            user_answer = int(user_answer)
        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return

        if user_answer == self.num1 + self.num2:
            feedback_image = Image.open("pic/good2.jpg")
            feedback_photo = ImageTk.PhotoImage(feedback_image)
            self.feedback_label.configure(image=feedback_photo)
            self.feedback_label.image = feedback_photo
            messagebox.showinfo("Result", "Good job!")
        else:
            feedback_image = Image.open("pic/bad.jpg")
            feedback_photo = ImageTk.PhotoImage(feedback_image)
            self.feedback_label.configure(image=feedback_photo)
            self.feedback_label.image = feedback_photo
            messagebox.showinfo("Result", f"Try again. The correct answer is {self.num1 + self.num2}.")
        self.entry.delete(0, tk.END)
        self.next_question()

    def next_question(self):
        self.generate_question()
        print('generated:', self.num1, self.num2)
        self.label.config(text=f"{self.num1} + {self.num2} = ?")
        if self.feedback_label:
            self.feedback_label.configure(image="")  # Reset feedback image

    def start_game(self):
        root = tk.Tk()
        root.title("Arithmetic Training")

        # Create widgets
        self.label = tk.Label(root, font=("Arial", 24))
        self.label.pack(pady=20)
        self.feedback_label = tk.Label(root)
        self.feedback_label.pack()
        self.entry = tk.Entry(root, font=("Arial", 24))
        self.entry.pack(pady=10)

        check_button = tk.Button(root, text="Check", command=self.check_answer, font=("Arial", 18))
        check_button.pack(pady=10)

        # Set the initial question
        self.next_question()

        # Bind the Enter key to the check_answer function
        root.bind('<Return>', lambda event: self.check_answer())

        # Start the GUI event loop
        root.mainloop()

if __name__ == '__main__':
    is_authorized = autho.login()
    if is_authorized:
        game = ArithmeticGame()
        game.start_game()
    print(is_authorized)
