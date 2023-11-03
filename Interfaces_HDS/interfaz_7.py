from tkinter import *
#C:\Users\Hp\Documents\CLASES JMA\Interfaces_HDS\JOSE_MARIA_ARGUEDAS_CON_NOMBRE-removebg-preview.png


ventanita = Tk()
ventanita.title('INTERFAZ_ 7')
ventanita.geometry('325x200')
 # TITULO DE CUADRO
etiqueta1 = Label(ventanita, text='CALCULAR _JMA', ) 
etiqueta1.config( fg='#006400',font=(30))
etiqueta1.grid()

# PRIMER CUADRO
etiqueta2 = Label(ventanita, text='INGRESAR PRIMER NUMERO:').grid(row=1, column=0)
num1 = Entry(ventanita)
num1.grid(row=2, column=0) 
# SEGUNDO CUADRO
etiqueta3= Label(ventanita, text='INGRESAR SEGUNDO NUMERO:').grid(row=3, column=0)
num2= Entry(ventanita)
num2.grid(row=4, column=0)
 # TERCER CUADRO
etiqueta4 = Label(ventanita, text='RESULTADO:').grid(row=5, column=0)
resultado = Entry(ventanita)
resultado.grid(row=6, column=0)

operacion = IntVar()
operacion.set(1)
# radiobutton SUMAS
radioSuma = Radiobutton(ventanita, text='SUMA', variable=operacion, value=1)
radioSuma.grid(row=1, column=3,columnspan=3)
# radiobutton RESTA
radioResta = Radiobutton(ventanita, text='RESTA', variable=operacion, value=2)
radioResta.grid(row=2, column=3,columnspan=2)
# radiobutton MULTIPLICAR
radioMultiplica = Radiobutton(ventanita, text='MULTIPLICAR', variable=operacion, value=3)
radioMultiplica.grid(row=3, column=3,)
# radiobutton 
radioDivide = Radiobutton(ventanita, text='DIVIDIR', variable=operacion, value=4)
radioDivide.grid(row=4, column=3)
# OPERACION
def calcular():
  n1 = int(num1.get()) 
  n2 = int(num2.get())
# SUMA
  if operacion.get() == 1:
    suma = n1 + n2
    resultado.delete(0, END)
    resultado.insert(0, str(suma))
#  RESTA
  elif operacion.get() == 2:
    resta = n1 - n2
    resultado.delete(0, END)
    resultado.insert(0, str(resta))  
# MULTIPLICAR
  elif operacion.get() == 3:
    multiplicacion = n1 * n2
    resultado.delete(0, END)
    resultado.insert(0, str(multiplicacion))
#  DIVIDICION
  elif operacion.get() == 4:
    division = n1 / n2
    resultado.delete(0, END)
    resultado.insert(0, str(division))


 #   OPCION CALCULAR
boton_Calcular = Button(ventanita, text="Calcular", command=calcular)
boton_Calcular.grid(row=8, column=0)

#  OPERACION PARA LIMPIAR
def limpiar():
  num1.delete(0,END)
  num2.delete(0,END)
  resultado.delete(0,END)
  num1.focus()
#  OPCION  LIMPIAR
boton_limpiar = Button(ventanita,text='Limpiar',command=limpiar).grid(row=8,column=1)

ventanita.mainloop()