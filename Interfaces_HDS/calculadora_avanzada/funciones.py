from tkinter import *
def enviar_boton(ventana,valor):
    if valor == "=":
        expresion=ventana.caja_operaciones.get().replace("%","/100")
        resultado=eval(expresion)
        ventana.caja_operaciones.delete(0,END)
        ventana.caja_operaciones.insert(0,str(resultado))
        operacion=expresion+" "+valor
        ventana.operacion_label.config(text=operacion)
    elif valor == "C":
        ventana.operacion_label.config(text="")
        ventana.caja_operaciones.delete(0,END)
    elif valor == "<":
        valor_actual=ventana.caja_operaciones.get()
        if valor_actual:
            nuevo_valor=valor_actual[:-1]
            ventana.caja_operaciones.delete(0,END)
            ventana.caja_operaciones.insert(0,nuevo_valor)
            ventana.operacion_label.config(text=nuevo_valor+" ")
    else:
        valor_actual=ventana.caja_operaciones.get()
        ventana.caja_operaciones.delete(0,END)
        ventana.caja_operaciones.insert(0,valor_actual+valor)
        if valor == "=":
            ventana.operacion_label.config(text="")

def cambio_tema(ventana,colores):
    if ventana.tema_oscuro:
        ventana.configure(bg=colores.COLOR_FONDO_LIGHT)
        ventana.caja_operaciones.config(fg=colores.COLOR_TEXTO_LIGHT,bg=colores.COLOR_CAJA_TEXTO_LIGHT)
        ventana.operacion_label.config(fg=colores.COLOR_TEXTO_LIGHT,bg=colores.COLOR_FONDO_LIGHT)
        ventana.boton_tema.configure(text="Modo Oscuro \uf181", relief=SUNKEN,bg=colores.COLOR_BOTONES_ESPECIALES_LIGHT)
    else:
        ventana.configure(bg=colores.COLOR_FONDO_NEGRO)
        ventana.caja_operaciones.config(fg=colores.COLOR_TEXTO_NEGRO,bg=colores.COLOR_CAJA_TEXTO_NEGRO)
        ventana.operacion_label.config(fg=colores.COLOR_TEXTO_NEGRO,bg=colores.COLOR_FONDO_NEGRO)
        ventana.boton_tema.configure(text="Modo claro \uf189", relief=SUNKEN,bg=colores.COLOR_BOTONES_ESPECIALES_NEGRO)
    ventana.tema_oscuro=not ventana.tema_oscuro