import tkinter as tk
from main_window import VorrexApp

window = tk.Tk()
window.geometry("1000x570")
window.title("Vorrex")
window.resizable(False, False)

app = VorrexApp(window)

window.mainloop()
