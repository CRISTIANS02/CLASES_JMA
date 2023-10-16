
#Importamos TKinter
from tkinter import *
 # creamos una clase
ventanita=Tk()
ventanita.geometry('400x400')
# creo mis  dos widgets de orden inferior ala clase frame()
Widget_uno=Frame()
Widget_uno.grid(row='0',column='0')
Widget_uno.config(width='400',height='100')
#Widget_uno.config(bg='red')

# creacion de etiquetas
etiqieta=Label(ventanita,text='ingresa su nombre: ')
etiqieta.grid(row=1,column=0)

#creacion de cuadro de texto
cuadro_texto=Entry(ventanita,bg='green')
cuadro_texto.grid(row=2,column=0)


ventanita.mainloop()