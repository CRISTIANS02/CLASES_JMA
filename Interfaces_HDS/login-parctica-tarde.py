# import tkinter as tk

# # Ventana principal 
# ventana = tk.Tk()
# ventana.title("Facebook")
# ventana.geometry("500x700")
# ventana.configure(bg="grey")

# # Función para verificar usuario y contraseña
# def verificar():
#     usuario = entrada_usuario.get()
#     contra = entrada_contra.get()
    
#     if usuario == "juan" and contra == "1234":
#         texto_bienvenida["text"] = "¡Bienvenido Juan!"
#     else:
#         texto_bienvenida["text"] = "Usuario o contraseña incorrectos"

# # Label superior 
# label_superior = tk.Label(ventana, text="facebook", bg="grey", fg="white", font=("Arial", 30))
# label_superior.pack(pady=20)

# # Cuadro para entrada de usuario
# entrada_usuario = tk.Entry(ventana, width=20, font=("Arial", 20))
# entrada_usuario.pack(pady=10)

# # Cuadro para entrada de contraseña  
# entrada_contra = tk.Entry(ventana, width=20, font=("Arial", 20), show="*") 
# entrada_contra.pack(pady=10)

# # Botón para verificar
# boton_verificar = tk.Button(ventana, text="Iniciar Sesión", font=("Arial", 20), command=verificar)
# boton_verificar.pack(pady=10)

# # Label para mensaje de bienvenida 
# texto_bienvenida = tk.Label(ventana, text="", font=("Arial", 15))
# texto_bienvenida.pack(pady=20)

#ventana.mainloop()
import tkinter as tk
from tkinter import *

# Create the main window
window = tk.Tk()
ventana = Tk()
window.title("iPad Screen")

# Set the size and position of the main window
window.geometry("600x800")
window.resizable(False, False)

# Create a frame for the iPad screen
ipad_frame = tk.Frame(window, width=500, height=700, bg="#f0f0f0")
ipad_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add widgets to the iPad screen
label = tk.Label(ipad_frame, text="Welcome to iPad", fg="black", bg="#f0f0f0", font=("Arial", 20, "bold"))
label.pack(pady=50)

button = tk.Button(ipad_frame, text="Click Me!", bg="blue", fg="white", font=("Arial", 16))
button.pack(pady=20)
def evaluar_login():
    usuario=1234
    contraseña=1234
    
    # usuario = usuario
    text_usuario = int(Text_usuario.get())
    text_contraseña=int(Text_contraseña.get())
    if text_usuario==usuario and text_contraseña==contraseña:
        mensaje = Label(ventana, text="BIENVENIDO AL MUNDO DE TODOS")
    else:
        mensaje = Label(ventana, text="ALERTA FBI")
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


# Run the main window loop
window.mainloop()