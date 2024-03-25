import tkinter as tk
from tkinter import ttk


class A(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')
        self._create_widgets()

    def _create_widgets(self):
        label1 = ttk.Label(text='Label1', relief=tk.SUNKEN, padding=0)
        label1.pack(expand=tk.YES, fill=tk.BOTH)

        label2 = ttk.Label(text='Label2', relief=tk.SUNKEN, padding=10)
        label2.pack(expand=tk.YES, fill=tk.BOTH)

        label3 = ttk.Label(text='Label3', relief=tk.SUNKEN, padding=50)
        label3.pack(expand=tk.YES, fill=tk.BOTH)


if __name__ == '__main__':
    window = A()
    window.mainloop()
