import datetime
COLOR_FONDO_PRIMARIO="#00CED1"
COLOR_FONDO_SECUNDARIO="#90EE90"
#COLOR_FONDO_TERCEARIO="FFF8DC"
COLOR_BOTON="#008000"
TITULO_APP="App de Contactos"
date=datetime.datetime.now()
HORA_ACTUAL=f"fecha: {date.day}-{date.month}-{date.year}, hora: {date.hour}:{date.minute}"

def centrar_ventana(ventana,ancho_ventana,largo_ventana):
    pantalla_ancho=ventana.winfo_screenwidth()
    pantalla_largo=ventana.winfo_screenheight()
    x=int((pantalla_ancho/2)-(ancho_ventana/2))
    y=int((pantalla_largo/2)-(largo_ventana/2))
    return ventana.geometry(f"{ancho_ventana}x{largo_ventana}+{x}+{y}")