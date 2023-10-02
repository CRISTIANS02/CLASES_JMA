# EJERCICIO N°1
import tkinter as tk

# Crear una ventana
ventana = tk.Tk()

# Personalizar la ventana
ventana.title("Mi Aplicación")
ventana.geometry("400x300")

# Agregar elementos a la ventana
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
etiqueta.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()



#EJEMPLO N° 2
import tkinter as tk
from tkinter import messagebox

# Función para mostrar un mensaje cuando se hace clic en el botón
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡HELLO , SAIRE!")

# Crear una ventana
ventana = tk.Tk()

# Personalizar la ventana
ventana.title("Ejemplo con Tkinter")
ventana.geometry("300x200")

# Crear un botón
boton = tk.Button(ventana, text="Haz clickea", command=mostrar_mensaje)
boton.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()





# EJEMPLO N°3
import tkinter as tk
from tkinter import messagebox

# Función para mostrar un mensaje personalizado cuando se hace clic en el botón
def mostrar_mensaje():
    nombre = entrada.get()  # Obtener el texto ingresado en el campo de entrada
    mensaje = f"Hola, {nombre}! ¡Bienvenido a Tkinter!"
    messagebox.showinfo("Mensaje Personalizado", mensaje)

# Crear una ventana
ventana = tk.Tk()

# Personalizar la ventana
ventana.title("Ejemplo Personalizado con Tkinter")
ventana.geometry("300x200")

# Crear un campo de entrada
entrada = tk.Entry(ventana)
entrada.pack()

# Crear un botón
boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()