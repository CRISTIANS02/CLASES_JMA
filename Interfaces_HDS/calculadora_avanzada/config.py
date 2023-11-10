# constante para el tema  oscuro
COLOR_FONDO_NEGRO="#1a1b28"
COLOR_TEXTO_BLANKO="white"
COLOR_BOTONES_ESPECIALES_NEGRO="#52c9dc"
COLOR_BOTONES_NEGRO="#1e2435"
COLOR_CAJA_TEXTO_NEGRO="#1a1b28"

# constante para el tema  claro
COLOR_FONDO_LIGHT="#ffffff"
COLOR_TEXTO_LIGHT="black"
COLOR_BOTONES_ESPECIALES_LIGHT="#52c9dc"
COLOR_BOTONES_LIGHT="#1e2435"
COLOR_CAJA_TEXTO_LIGHT="#ffffff"

#funcion que nos permite centrar nuestra pantalla:
def centrar_ventana(ventana,ancho_ventana,largo_ventana):
    pantalla_ancho=ventana.winfo_screenwidth()
    pantalla_largo=ventana.winfo_screenheight()
    x=int((pantalla_ancho/2)-(ancho_ventana/2))
    y=int((pantalla_largo/2)-(largo_ventana/2))
    return ventana.geometry(f"{ancho_ventana}x{largo_ventana}+{x}+{y}")
