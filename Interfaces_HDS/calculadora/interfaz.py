from tkinter import*
from funciones import*
root=Tk()
root.title("Calculadora")
root.geometry("300x300")
root.resizable(0,0)
#####
fuente_general=("arial",8,"bold")
# pantalla que muestra lso numero ingredaso  y el resultado
pantalla=Entry(root,width=22,
               bg="black",  # asigna color de fondo
               fg="white",  # asigna el color de letra
               borderwidth=0,   # tamaño del borde de mi cuadro de texto
               font=("arial",18,"bold"))    # asignarles el tipo tamaño de fuente
pantalla.grid(row=0,columnspan=4,padx=4,pady=4)
# añadir los botones de mi calculadora

boton_1=Button(root,text="1",
               width=9,
               height=3,
               bg="white",
               fg="red",
               borderwidth=0,
               cursor="hand2",font=fuente_general,command=lambda:enviar_boton(1,pantalla)).grid(row=1,column=0,padx=1,pady=1) # cursor -> sirve al momento de pasar por el botton a un cursor en forma de mano
boton_2=Button(root,text="2",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(2,pantalla)).grid(row=1,column=1,padx=1,pady=1)
boton_3=Button(root,text="3",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(3,pantalla)).grid(row=1,column=2,padx=1,pady=1)
boton_4=Button(root,text="4",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(4,pantalla)).grid(row=2,column=0,padx=1,pady=1)
boton_5=Button(root,text="5",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(5,pantalla)).grid(row=2,column=1,padx=1,pady=1)
boton_6=Button(root,text="6",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(6,pantalla)).grid(row=2,column=2,padx=1,pady=1)
boton_7=Button(root,text="7",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(7,pantalla)).grid(row=3,column=0,padx=1,pady=1)
boton_8=Button(root,text="8",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(8,pantalla)).grid(row=3,column=1,padx=1,pady=1)
boton_9=Button(root,text="9",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(9,pantalla)).grid(row=3,column=2,padx=1,pady=1)
boton_10=Button(root,text="0",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(0,pantalla)).grid(row=4,column=1,padx=1,pady=1)

# boton.
boton_punto=Button(root,text=".",width=9,height=3,bg="spring green",fg="white",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(".",pantalla)).grid(row=4,column=0,padx=1,pady=1)
# boton ygual
boton_igual=Button(root,text="=",width=9,height=3,bg="red",fg="black",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:igual(pantalla)).grid(row=4,column=2,padx=1,pady=1)
# boton de operaciones
boton_suma=Button(root,text="+",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:operacion("+",pantalla)).grid(row=1,column=3,padx=1,pady=1)
boton_menos=Button(root,text="-",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:operacion("-",pantalla)).grid(row=2,column=3,padx=1,pady=1)
boton_multiplicacion=Button(root,text="x",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:operacion("*",pantalla)).grid(row=3,column=3,padx=1,pady=1)
boton_dividir=Button(root,text="/",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:operacion("/",pantalla)).grid(row=4,column=3,padx=1,pady=1)
# boton limpiar
boton_limpiar=Button(root,text="Limpiar",width=9,height=3,bg="green",fg="black",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:limpiar(pantalla)).grid(row=5,column=0,columnspan=4,padx=4,pady=1,sticky=W+E)

root.mainloop()
