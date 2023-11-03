from tkinter import *
ventana=Tk()
ventana.geometry()
## clase operadores
class operadores:
    def sumar(self,num1,num2):
        return num1+num2
    def resta(self,num1,num2):
        return num1-num2
    def multiplicar(self,num1,num2):
        return num1*num2
    def dividir(self,num1,num2):
        return num1/num2
## manejador de operaciones
operacion=StringVar()
classOperadores=operadores()
def manejadorOperadores():
    num1=int(textoUno.get())
    num2=int(textoDos.get())
    ope=operacion.get()
    if ope=='suma':
        resultado=classOperadores.sumar(num1,num2)
        Label (ventana,text=f' el resultado de la suma es : {resultado}').pack()
    elif ope=='resta':
        resultado=classOperadores.sumar(num1,num2)
        Label (ventana,text=f' el resultado de la suma es : {resultado}').pack()
    elif ope=='multiplicar':
        resultado=classOperadores.sumar(num1,num2)
        Label (ventana,text=f' el resultado de la suma es : {resultado}').pack()
    elif ope=='dividir':
        resultado=classOperadores.sumar(num1,num2)
        Label (ventana,text=f' el resultado de la suma es : {resultado}').pack()
    
        
    
    
