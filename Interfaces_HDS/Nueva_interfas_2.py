# IMPORT TKinter 
from tkinter import* 
#Instanciar la clase de tk()
ventana=Tk()
# Creo mis dos  widget de una orden inferior con la clase frame()

# Instancio mi primer widget
Widget_dos=Frame()
# Usar el metodo para montar el frame
# Widget_uno.grid(row='0',column='0')
# Widget_uno.config(width='100'),height='100'
# Widget_uno.config(bg='yellow')
# # El metodo grid recibe dos parametros el numero de la columna y el numero de la fila de la creacion  del segundo widget
# Widget_dos=Frame()  
# Widget_dos.grid(row='2',column='0')
# Widget_uno.config(width='100'),height='100'
# Widget_uno.config(bg='purple')
# Usar el metodo de loop para que la ventana permanesca abierta
ventana.mainloop()
