import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
import re

class FileWordCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Word Counter")
        self.master.geometry("500x500")
        self.master.config(bg="#f0f4c3")

        self.title = tk.Label(master, text="📁 Select a Text File", font=("Segoe UI", 16, "bold"), bg="#f0f4c3")
        self.title.pack(pady=10)

        self.select_button = tk.Button(master, text="Browse File", command=self.browse_file, font=("Segoe UI", 12), bg="#388e3c", fg="white")
        self.select_button.pack(pady=10)

        self.result_box = tk.Text(master, height=20, width=55, font=("Consolas", 10))
        self.result_box.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset, font=("Segoe UI", 11), bg="#f44336", fg="white")
        self.reset_button.pack(pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read().lower()
                    words = re.findall(r'\b\w+\b', text)
                    word_counts = Counter(words)
                    sorted_counts = dict(sorted(word_counts.items()))

                    self.result_box.delete("1.0", tk.END)
                    self.result_box.insert(tk.END, f"📊 Word Count Results:\n{'-'*40}\n")
                    for word, count in sorted_counts.items():
                        self.result_box.insert(tk.END, f"{word:<15}: {count}\n")
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file.\n\n{e}")

    def reset(self):
        self.result_box.delete("1.0", tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FileWordCounterApp(root)
    root.mainloop()