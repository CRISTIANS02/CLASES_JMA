import tkinter as tk

root = tk.Tk()

# Create 2 blue squares on top
for i in range(2):
    square = tk.Canvas(root, width=50, height=50, bg='blue')
    square.grid(row=0, column=i)

# Create a green rectangle below
green_rect = tk.Canvas(root, width=00, height=50, bg='green')
green_rect.grid(row=1, column=0, columnspan=2)

# Create a red rectangle below the green rectangle
red_rect = tk.Canvas(root, width=100, height=50, bg='red')
red_rect.grid(row=2, column=0, columnspan=2)

# Create 4 red squares at the bottom
for i in range(4):
    square = tk.Canvas(root, width=50, height=50, bg='red')
    square.grid(row=3, column=i)

root.mainloop()