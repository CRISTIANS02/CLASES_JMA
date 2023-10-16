#Importamos TKinter
from tkinter import *
 # creamos una clase
windows=Tk()
windows.geometry('300x400')

# Widget_uno=Frame()
# Widget_uno.grid(row='1',column='1')
# Widget_uno.config(width='50',height='100')
# #Widget_uno.config(bg='red')

#ETIQUETA 1
etiqieta=Label(windows,text='INGRESE SU NOMBRE: ')
etiqieta.grid(row=1,column=0)

cuadro_texto=Entry(windows,bg='green')
cuadro_texto.grid(row=1,column=1)

# ETIQUETA 2
etiqieta=Label(windows,text='DNI: ')
etiqieta.grid(row=2,column=0)

cuadro_texto=Entry(windows,bg='green')
cuadro_texto.grid(row=2,column=1)

# ETIQUETA 3
etiqieta=Label(windows,text='CELULAR: ')
etiqieta.grid(row=3,column=0)

cuadro_texto=Entry(windows,bg='green')
cuadro_texto.grid(row=3,column=1)

# CREACION DEL CUADRO

Widget_cuadro=Frame()
Widget_cuadro.grid(row='4',column='0',)
Widget_cuadro.config(width='15',height='7')


Widget_uno=Frame()
Widget_uno.grid(row='5',column='0',columnspan=2)
Widget_uno.config(width='270',height='180')
Widget_uno.config(bg='yellow')


Widget_cuadro=Frame()
Widget_cuadro.grid(row='6',column='0',)
Widget_cuadro.config(width='180',height='70')

Widget_cuadro=Frame()
Widget_cuadro.grid(row='7',column='0',columnspan=2)
Widget_cuadro.config(width='300',height='190')


windows.mainloop()



