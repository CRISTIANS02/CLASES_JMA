from tkinter import *
from tkinter.messagebox import *

def f_limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)

    ventana.nombre_texto.focus()

def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellido=ventana.apellidos_texto.get()
    celular=ventana.celular_texto.get()
    ventana.tabla_datos.insert("",END,text=nombre,values=(apellido,celular))
    showinfo(title="Nuevo",message="Nuevo contacto agregado")
    f_limpiar(ventana)

def f_eliminar(ventana):
    item_seleccionado = ventana.tabla_datos.selection()
    print(item_seleccionado)
    if item_seleccionado:
        ventana.tabla_datos.delete(item_seleccionado)
        showwarning(title="ELIMINAR",message="Registro elimnado")
        f_limpiar(ventana)
    else:
        print("Selecciona una fila para eliminar.")

def f_actualizar(ventana):
    if ventana.nombre_texto.get()=="":
        showerror(title="SIN DATOS",message="Eres huevon no hay nada para actualizar")
    else:
        nombre=ventana.nombre_texto.get()
        apellidos=ventana.apellidos_texto.get()
        celular=ventana.celular_texto.get()
        elem_actualizar=ventana.tabla_datos.selection()
        mensaje=askyesno(title="Actualizar",message="Estas seguro que deseas actualizar")
        if mensaje == True:
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)
            return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,celular))
        else:
            showinfo(title="NO ACTUALIZO",message="No se actualizo ningun registro")
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)

def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askyesno(title="ACTUALIZAR",message="Desea actualizar los datos")
    if mensaje == True:
        nombre=captura_datos["text"]
        apellidos=captura_datos["values"][0]
        celular=captura_datos["values"][1]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apellidos_texto.insert(0,apellidos)
        ventana.celular_texto.insert(0,celular)
        #ventana.tabla_datos.selection_remove(elem_actualizar)
    else:
        showinfo(title="ACTUALIZAR",message="Ningun registro seleccionado para actualizar")
        #ventana.tabla_datos.selection_remove(elem_actualizar)   
    