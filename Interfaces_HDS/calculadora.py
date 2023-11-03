from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

# Pantalla de resultado arriba
resultado = Entry(ventana, width=35) 
resultado.grid(row=0, column=0, columnspan=5)

# Función para capturar el clic del botón
def capturar(numero):
    resultado.insert(END, numero)

# Botones de 1 a 9 en filas 3 a 5
boton1 = Button(ventana, text="1", width=5, height=2, command=lambda: capturar(1))
boton1.grid(row=2, column=0)
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda: capturar(2))
boton2.grid(row=2, column=1)
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda: capturar(3))
boton3.grid(row=2, column=2)
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda: capturar(4))
boton4.grid(row=3, column=0)
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda: capturar(5))
boton5.grid(row=3, column=1)
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda: capturar(6))
boton6.grid(row=3, column=2)
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda: capturar(7))
boton7.grid(row=4, column=0)
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda: capturar(8))
boton8.grid(row=4, column=1)
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda: capturar(9))
boton9.grid(row=4, column=2)
boton0 = Button(ventana, text="0", width=5, height=2, command=lambda: capturar(0))
boton0.grid(row=5, column=0)

# Función para realizar la operación
def realizar_operacion(operador):
    num1 = int(resultado.get())
    resultado.delete(0, END)
    if operador == "=":
        resultado.insert(END, eval(num1))
    else:
        resultado.insert(END, operador)

# Botones de operaciones en fila 2
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda: realizar_operacion("+"))
boton_suma.grid(row=2, column=3)
boton_resta = Button(ventana, text="-", width=5, height=2, command=lambda: realizar_operacion("-"))
boton_resta.grid(row=3, column=3)
boton_multi = Button(ventana, text="*", width=5, height=2, command=lambda: realizar_operacion("*"))
boton_multi.grid(row=4, column=3) 
boton_divi = Button(ventana, text="/", width=5, height=2, command=lambda: realizar_operacion("/"))
boton_divi.grid(row=5, column=3)
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda: realizar_operacion("="))
boton_igual.grid(row=5, column=1, columnspan=2)

# Botón borrar abajo
def borrar():
    resultado.delete(0, END)

boton_borrar = Button(ventana, text="CLEAR", width=36, height=2, command=borrar)
boton_borrar.grid(row=6, column=0, columnspan=5)

ventana.mainloop()