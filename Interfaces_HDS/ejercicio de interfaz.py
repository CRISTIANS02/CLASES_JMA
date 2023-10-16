import tkinter as tk

root = tk.Tk()

# primer cuadro azul
for i in range(1):
    cuadro = tk.Canvas(root, width=50, height=50, bg='blue')
    cuadro.grid(row=0, column=0)
# segundo cuadro azul
    
for i in range(1):
    cuadro = tk.Canvas(root, width=50, height=50, bg='blue')
    cuadro.grid(row=0, column=1)
# tercer rectángulo verde 
rectangulo_verde = tk.Canvas(root, width=100, height=50, bg='green')
rectangulo_verde.grid(row=1, column=i, columnspan=2)

# cuarto rectángulo rojo 
rectangulo_rojo = tk.Canvas(root, width=100, height=50, bg='red')
rectangulo_rojo.grid(row=2, column=i, columnspan=2)

# quintt 4 cuadros rojos 
for i in range():
    cuadro = tk.Canvas(root, width=50, height=50, bg='red')
    cuadro.grid(row=3, column=i)

root.mainloop()