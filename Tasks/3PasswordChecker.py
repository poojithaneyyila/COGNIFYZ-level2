import tkinter as tk
from tkinter import ttk
import string
import re

class PasswordStrengthChecker:
    def __init__(self, master):
        self.master = master
        self.master.title("🔐 Password Strength Checker")
        self.master.geometry("400x350")
        self.master.config(bg="#e3f2fd")

        self.label = tk.Label(master, text="Enter Your Password:", font=("Segoe UI", 12), bg="#e3f2fd")
        self.label.pack(pady=10)

        self.password_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.password_var, show="*", font=("Segoe UI", 12), width=30)
        self.entry.pack()

        self.show_var = tk.IntVar()
        self.show_check = tk.Checkbutton(master, text="Show Password", variable=self.show_var,
                                         command=self.toggle_password, bg="#e3f2fd")
        self.show_check.pack()

        self.check_btn = tk.Button(master, text="Check Strength", font=("Segoe UI", 11),
                                   bg="#1976d2", fg="white", command=self.check_strength)
        self.check_btn.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Segoe UI", 12, "bold"), bg="#e3f2fd")
        self.result_label.pack()

        self.suggestions = tk.Label(master, text="", font=("Segoe UI", 10), bg="#e3f2fd", justify="left")
        self.suggestions.pack(pady=10)

    def toggle_password(self):
        if self.show_var.get():
            self.entry.config(show="")
        else:
            self.entry.config(show="*")

    def check_strength(self):
        password = self.password_var.get()
        score, feedback, color = self.analyze_password(password)

        self.result_label.config(text=f"Strength: {feedback}", fg=color)

        suggestions = self.get_suggestions(password)
        self.suggestions.config(text="\n".join(suggestions) if suggestions else "✅ Your password is strong!")

    def analyze_password(self, password):
        score = 0
        length = len(password) >= 8
        upper = re.search(r'[A-Z]', password)
        lower = re.search(r'[a-z]', password)
        digit = re.search(r'\d', password)
        special = re.search(rf"[{re.escape(string.punctuation)}]", password)

        if length: score += 1
        if upper: score += 1
        if lower: score += 1
        if digit: score += 1
        if special: score += 1

        if score == 5:
            return score, "Strong 💪", "green"
        elif 3 <= score < 5:
            return score, "Moderate ⚠", "orange"
        else:
            return score, "Weak ❌", "red"

    def get_suggestions(self, password):
        suggestions = []
        if len(password) < 8:
            suggestions.append("• Use at least 8 characters.")
        if not re.search(r'[A-Z]', password):
            suggestions.append("• Add at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            suggestions.append("• Add at least one lowercase letter.")
        if not re.search(r'\d', password):
            suggestions.append("• Include at least one digit.")
        if not re.search(rf"[{re.escape(string.punctuation)}]", password):
            suggestions.append("• Use special characters like @, #, $, etc.")
        return suggestions

# Run the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()