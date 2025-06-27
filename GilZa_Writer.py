#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox

class GilZaWriter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GilZa Writer")
        self.geometry("800x600")

        self.text = tk.Text(self, wrap='word', font=("Fira Code", 14))
        self.text.pack(fill='both', expand=True)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)

        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Exit", command=self.quit)

        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, content)
                self.title(f"GilZa Writer - {path}")
            except Exception as e:
                messagebox.showerror("Error", f"Can't open file: {e}")

    def save_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    content = self.text.get('1.0', tk.END)
                    f.write(content)
                self.title(f"GilZa Writer - {path}")
            except Exception as e:
                messagebox.showerror("Error", f"Can't save file: {e}")

if __name__ == "__main__":
    app = GilZaWriter()
    app.mainloop()
