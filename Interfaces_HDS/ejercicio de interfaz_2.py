# import tkinter as tk

# root = tk.Tk()

# # primer cuadro azul
# for i in range(2):
#     cuadro = tk.Canvas(root, width=50, height=50, bg='blue')
#     cuadro.grid(row=0, column=0)
# # segundo cuadro azul
    
# for i in range(2):
#     cuadro = tk.Canvas(root, width=50, height=50, bg='red')
#     cuadro.grid(row=1, column=1)
    
# for i in range(2):
#     cuadro = tk.Canvas(root, width=50, height=50, bg='orange')
#     cuadro.grid(row=2, column=2)
    

import tkinter as tk

root = tk.Tk()

# primer cuadro azul
for i in range(1):
    cuadro = tk.Canvas(root, width=50, height=100, bg='red')
    cuadro.grid(row=0, column=0,rowspan=2)
       

    cuadro = tk.Canvas(root, width=50, height=50, bg='green')
    cuadro.grid(row=0, column=1)
# tercer rectángulo verde 
# for i in range(1):
#     cuadro = tk.Canvas(root, width=50, height=50, bg='yellow')
#     cuadro.grid(row=1, column=0)
       

    cuadro = tk.Canvas(root, width=50, height=50, bg='blue')
    cuadro.grid(row=1, column=1)
    
# tercero

    cuadro = tk.Canvas(root, width=100, height=50, bg='green')
    cuadro.grid(row=2, column=0,columnspan=2)

    
# for i in range(1):
#     cuadro = tk.Canvas(root, width=50, height=50, bg='orange')
#     cuadro.grid(row=2, column=1)

root.mainloop()