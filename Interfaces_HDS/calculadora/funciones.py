from tkinter import *
def enviar_boton(valor,pantalla):
    anterior =pantalla.get()
    pantalla.delete(0,END)
    pantalla.insert(0,str (anterior)+str(valor))
#suma
def operacion(signo,pantalla):
    global num1
    global signo_op
    num1=pantalla.get()
    num1=float(num1)
    pantalla.delete(0,END)
    signo_op=signo
    
def igual(pantalla):
    global num2
    num2=pantalla.get()
    pantalla.delete(0,END)
    match signo_op:
        case'+': 
         pantalla.insert(0,num1 + float(num2))
        case'-': 
         pantalla.insert(0,num1 - float(num2))
        case'*': 
         pantalla.insert(0,num1 * float(num2))
        case'/': 
         pantalla.insert(0,num1 / float(num2))
         
         
def limpiar(pantalla):
    pantalla.delete(0,END)