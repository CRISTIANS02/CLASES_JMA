from tkinter import *

ventana = Tk()
ventana.geometry("350x400")
ventana.title('Verificación de edad')

def evaluar_edad():
    edad = int(Text_edad.get())
    if edad < 18:
        mensaje = Label(ventana, text="Eres menor de edad")
    else:
        mensaje = Label(ventana, text="Eres mayor de edad")
    mensaje.pack()

etiqueta = Label(ventana, text='Ingresa tu edad:')
etiqueta.pack()

Text_edad = Entry(ventana)
Text_edad.config(bg='orange', fg='black')
Text_edad.pack()

boton_evaluar = Button(ventana, text='Evaluar', command=evaluar_edad)
boton_evaluar.pack()

ventana.mainloop()