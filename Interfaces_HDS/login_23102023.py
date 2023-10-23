from tkinter import *

ventana = Tk()
ventana.geometry("350x400")
ventana.title('INICIAR SECION')

def evaluar_login():
    usuario=1234
    contraseña=1234
    
    # usuario = usuario
    text_usuario = int(Text_usuario.get())
    text_contraseña=int(Text_contraseña.get())
    if text_usuario==usuario and text_contraseña==contraseña:
        mensaje = Label(ventana, text="BIENVENIDO AL MUNDO DE TODOS")
    else:
        mensaje = Label(ventana, text="LARGATE AL INFIERNO")
    mensaje.pack()
    


# USUARIO
etiqueta = Label(ventana, text='INGRESA TU USUARIO:')
etiqueta.pack()

Text_usuario = Entry(ventana)
Text_usuario.config(bg='orange', fg='black')
Text_usuario.pack()

# CONTRASEÑA
etiqueta = Label(ventana, text='INGRESA TU CONTRASEÑA:')
etiqueta.pack()

Text_contraseña = Entry(ventana)
Text_contraseña.config(bg='orange', fg='black',show='*')
Text_contraseña.pack()

boton_evaluar = Button(ventana, text='INGRESAR', command=evaluar_login)
boton_evaluar.pack()

ventana.mainloop()