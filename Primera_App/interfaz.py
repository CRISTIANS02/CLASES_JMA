from tkinter import *
from tkinter import ttk
from config import *
from funciones import *

class InterfazApp(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.construir_widget()

    #metodo propio vamos a darle las configuraciones basicas para mostrar nuestra ventana
    def configurar_ventana(self):
        self.title(f"{TITULO_APP} {HORA_ACTUAL}")
        self.configure(bg=COLOR_FONDO_PRIMARIO)
        self.resizable(0,0)
        self.attributes("-alpha",0.96)
        w,h=870,400
        centrar_ventana(self,w,h)

    def construir_widget(self):
        #CAJITA DE TEXTOS
        self.cajas_textos=LabelFrame(self,text="Cajas de texto",width=150,height=360,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.cajas_textos.grid(row=0,column=0,pady=20,padx=20)
        #caja para capturar el nombre
        self.label_nombre=Label(self.cajas_textos,text="Nombres",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.nombre_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.nombre_texto.pack()
        #caja para capturar el apellido
        self.label_apellido=Label(self.cajas_textos,text="Apellidos",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.apellidos_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.apellidos_texto.pack()
        #caja para capturar el Nro de celular
        self.label_celular=Label(self.cajas_textos,text="Nro Celular",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.celular_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.celular_texto.pack()
        #FIN CAJITA DE TEXTOS
        #CAJITA DE BOTONES
        self.cajas_botones=LabelFrame(self,text="Cajas de botones",width=150,height=430,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.cajas_botones.grid(row=0,column=1,pady=20,padx=20)
        #boton nuevo
        self.nuevo=Button(self.cajas_botones,command=lambda:f_nuevo(self),text="Nuevo",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #boton actualizar
        self.actualizar=Button(self.cajas_botones,command=lambda: f_actualizar(self),text="Actualizar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #boton eliminar
        self.eliminar=Button(self.cajas_botones,command=lambda:f_eliminar(self),text="Eliminar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #boton cancelar
        self.cancelar=Button(self.cajas_botones,command=lambda:f_limpiar(self),text="Cancelar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #FIN CAJITA DE BOTONES
        #TABLA DE DATOS
        self.caja_datos=LabelFrame(self,text="Caja de Datos",width=600,height=360,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.caja_datos.grid(row=0,column=2,pady=20,padx=20)

        #tabla
        self.tabla_datos=ttk.Treeview(self.caja_datos,columns=("#1","#2"))
        self.tabla_datos.column("#0",width=40)
        self.tabla_datos.column("#1",width=120)
        self.tabla_datos.column("#2",width=40)

        self.tabla_datos.heading("#0",text="Nombres")
        self.tabla_datos.heading("#1",text="Apellidos")
        self.tabla_datos.heading("#2",text="Celular")
        alumnitos=[
            ("moises","peñadira","564646441"),
            ("tarantula","medafiel","987654321"),
            ("maria","de jory","9877854321"),
            ("nadine","guadalupe","98888654321")
        ]
        for nom,ape,cel in alumnitos:
            self.tabla_datos.insert("",END,text=nom,values=(ape,cel))
        
        self.tabla_datos.bind("<Double-1>",lambda event:f_dobleClick(self,event))
        self.tabla_datos.place(x=0,y=0,width=400,height=600)
        #FIN DE TABLA DE DATOS