
# EL NOMBRE  NOMBRE SIEMPRE DEBERA SER EN SINGULAR Y CON LA PRIMERA LETRA MAYUSCULA
class Perro:
    nombre='boby'
    edad='2 meses'
    color='checche'
    raza='chestereir'
    
    def ladrar(self):
        return' guau guau'
    def corre(self,pasos):
        huevo=f'corriste{pasos},pasos'
        return huevo
    # aqui creamos un aclase segun UMl

respuesta=Perro()
print(respuesta.nombre)
print(respuesta.ladrar())
print(respuesta.corre(10))