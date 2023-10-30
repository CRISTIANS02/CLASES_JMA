# primero importamos lalibreria
from tkinter import *

# iniciamos nuestra clase tk()

ventana=Tk () # clase para crear un una ventana
ventana.title('clase radiobutton') # hacuendo usio del metodo title para el titulo de mi ventana
ventana.geometry('400x300') # mhaciendo uso del metodo geometry para asignarle tamaño a u aventana

# instancia mi clase  label
etiqueta=Label(ventana,text='radio buttons')#  clase paracrear una etiqueta
#  indicar la parte de mi ventana que deso que me muestre
# puedo usar los metodos grid o pack
etiqueta.config(fg='#EB6828',font=(50))
etiqueta.pack()

info=IntVar()
def mostra_radio():
    print(info.get())

# instranciar la clase radiobutton
radioMasculino=Radiobutton(ventana,text='Masculino',value=1,variable=info)
radioMasculino.pack()
radioFemenino=Radiobutton(ventana,text='Femenino',value=0,variable=info)
radioFemenino.pack()
radiolosdos=Radiobutton(ventana,text='PREFIERE NO DECIRLO ',value=3,variable=info)
radiolosdos.pack()

#instanciar la clasebutton
boton=Button(ventana,text='enviar',command=mostra_radio)
boton.pack()


# Función para mostrar un mensaje cuando se hace clic en el botón

def mostrar_radio():
    #  respuesta='Eres masculino' if info.get()==1 else "eres femenino"
    #  etiquetaRespuesta=Label(ventana,text=respuesta)
    #  etiquetaRespuesta.pack()
     
     if info.get()==1:
         etiquetRespuesta=Label(ventana,text="eres masculino")
         etiquetRespuesta.pack()
    
     else:
        etiquetaRespuesta=Label(ventana,text="eres femenino")
        etiquetaRespuesta
    

 
        
        

## llamar  al metodo de tk  que me permite tener persistenacia al  mostar la ventana
ventana.mainloop()
