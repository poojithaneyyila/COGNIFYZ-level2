import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("350x300")
        self.master.config(bg="#f0f8ff")

        self.target = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="🎯 Guess a number (1–100)", font=("Segoe UI", 14, "bold"), bg="#f0f8ff")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Segoe UI", 12))
        self.entry.pack()

        self.check_button = tk.Button(master, text="Check", font=("Segoe UI", 12), command=self.check_guess)
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Segoe UI", 12), bg="#f0f8ff")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset Game", font=("Segoe UI", 10), command=self.reset_game)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.target:
                self.result_label.config(text="Too low! Try again.", fg="blue")
            elif guess > self.target:
                self.result_label.config(text="Too high! Try again.", fg="orange")
            else:
                self.result_label.config(text=f"🎉 Correct! You guessed in {self.attempts} attempts!", fg="green")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.", fg="red")

    def reset_game(self):
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="", fg="green")

# Launch the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()