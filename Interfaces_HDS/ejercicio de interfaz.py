import tkinter as tk

def create_square(color):
    square = tk.Canvas(root, width=150, height=108, bg=color)
    square.pack(side=tk.LEFT, padx=5)

root = tk.Tk()

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

for color in colors:
    create_square(color)

root.mainloop()