from tkinter import *
from tkinter import messagebox
 # creamos una clase
class App():
    def __init__(self):
        # creamos el objeto de tiopo tkinter
        ventana=Tk()
        ventana.title('ventana principal')
        ventana.geometry('400x400')
        #ventana.configure(bg='green')
        
        
        #widgtes
        self.label1=Label(ventana,text='nombre')
        self.Label1,Place(x=20,y=30)
        
        self.text1=Entry(ventana,bg='red')
        self.text1,Place(x=100,y=30)
        
        #buttons
        
        
        self.bt1=Button(ventana,text='Aceptar',command=self.mensaje)
        self.bt1,Place(x=60,y=80)
        
        
        
        ventana.mainloop()
        
        
    def mensaje(self):
        #print('Buenvenido al sistema')
        messagebox.showinfo(message='BIENVENIDO AL SISTEMA',title='Ejemplo de mensaje')
        
        
# programa principal
objecto_ventana = App()