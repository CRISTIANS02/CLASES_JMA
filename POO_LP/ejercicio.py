#crear un objeto haciendo uso de la POO crear un objeto para cda edentidad celular

class IPHONE:
    modelo='PRO MAX 12'
    EMEI='132546789563'
    color='dorado'
    operadora='bitel'
    
    def llamar(self):
        return' rin rin rin tin tin tin tink'
    def fotos(self,pasos):
        huevo=f'corriste{pasos},pasos'
        return huevo
    # aqui creamos un aclase segun UMl

# respuesta=Perro()
# print(respuesta.nombre)
# print(respuesta.ladrar())
# print(respuesta.corre(10

# haciendo uso de la POO crear un objeto para la edentidad vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

coche = Vehiculo("Toyota", "Corolla", 2021)
coche.mostrar_info()


# haciendo uso de la POO crear un objeto para la edintidad avion
class Avion:
    def __init__(self, modelo, capacidad, velocidad_maxima):
        self.modelo = modelo
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")

avion1 = Avion("Boeing 747", 416, 988)
avion1.mostrar_informacion()




# haciendo uso de la POO crear un objeto para la edintidad dota 2





## TKINTER .- LIBRERIA  DE PYTHON PARA LA CREACION DE  INTERFAZ GRAFICAS 