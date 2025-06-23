import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg="#e1f5fe")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label_title = tk.Label(master, text="🎯 Guess the Number (1-100)", font=("Segoe UI", 16), bg="#e1f5fe")
        self.label_title.pack(pady=10)

        self.entry = tk.Entry(master, font=("Segoe UI", 14), justify='center')
        self.entry.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Segoe UI", 12), bg="#e1f5fe")
        self.result_label.pack(pady=10)

        self.attempts_label = tk.Label(master, text="Attempts: 0", font=("Segoe UI", 12), bg="#e1f5fe")
        self.attempts_label.pack(pady=5)

        self.submit_btn = tk.Button(master, text="Submit Guess", font=("Segoe UI", 12), command=self.check_guess, bg="#4caf50", fg="white")
        self.submit_btn.pack(pady=5)

        self.reset_btn = tk.Button(master, text="Reset Game", font=("Segoe UI", 12), command=self.reset_game, bg="#f44336", fg="white")
        self.reset_btn.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().strip()
        if not guess.isdigit():
            self.result_label.config(text="❌ Please enter a valid number!", fg="red")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.target_number:
            self.result_label.config(text="Too low! Try again.", fg="orange")
        elif guess > self.target_number:
            self.result_label.config(text="Too high! Try again.", fg="orange")
        else:
            self.result_label.config(
                text=f"🎉 Correct! You guessed it in {self.attempts} attempts.",
                fg="green"
            )

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="", fg="black")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()