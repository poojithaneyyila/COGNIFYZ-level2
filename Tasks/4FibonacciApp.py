import tkinter as tk
from tkinter import messagebox

class FibonacciApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fibonacci Sequence Generator")
        self.master.geometry("400x350")
        self.master.config(bg="#e3f2fd")

        # Label
        self.label = tk.Label(master, text="Enter number of terms:", font=("Segoe UI", 14, "bold"), bg="#e3f2fd")
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(master, font=("Segoe UI", 12), justify="center")
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(master, text="Generate Fibonacci", command=self.generate_fibonacci, font=("Segoe UI", 12), bg="#1976d2", fg="white")
        self.button.pack(pady=10)

        # Result display
        self.result_text = tk.Text(master, height=5, width=40, font=("Segoe UI", 11))
        self.result_text.pack(pady=10)

        # Reset Button
        self.reset_btn = tk.Button(master, text="Reset", command=self.reset, font=("Segoe UI", 10), bg="#f44336", fg="white")
        self.reset_btn.pack()

    def generate_fibonacci(self):
        self.result_text.delete("1.0", tk.END)
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError
            sequence = self.get_fibonacci_sequence(n)
            self.result_text.insert(tk.END, "➡ Fibonacci Sequence:\n")
            self.result_text.insert(tk.END, " ".join(map(str, sequence)))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")

    def get_fibonacci_sequence(self, n):
        sequence = []
        a, b = 0, 1
        for _ in range(n):
            sequence.append(a)
            a, b = b, a + b
        return sequence

    def reset(self):
        self.entry.delete(0, tk.END)
        self.result_text.delete("1.0", tk.END)

# Launch App
if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()