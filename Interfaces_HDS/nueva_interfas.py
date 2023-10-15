#1 import tkinter: Libreria para la creacion de interfaces grafica
from tkinter import *
# la libreria tkinter tiene trees grandes clases para la creacion de interfaces
#tk()
#tkk()
#Tcl()
#2. INSTANCIAR  Tk () como generador de interfas grafica
nueva_ventana=Tk()
## Frame  es tambien una clase frame( ) para la crear una frame tengo que primero instanciar
menu_principal=Frame
#Montamos o inicialisamos el frame
menu_principal.pack()
#Haciendo el uso del metodo config le damos un tamaño
menu_principal.config(width='200',heigth='200')
#Haciendomuso del metodo config le asignamos el color
menu_principal.config(bg='red')
# Metodo de tk() que mantiene la ejecucion de un programa en un bucle
nueva_ventana.mainloop




