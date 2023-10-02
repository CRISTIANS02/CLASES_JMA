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

class Dota2Entity:
    def __init__(self, name, role, attack_type):
        self.name = name
        self.role = role
        self.attack_type = attack_type

# Crear un objeto Dota 2
dota_hero = Dota2Entity("Anti-Mage", "Carry", "Melee")

# Acceder a los atributos del objeto
print(dota_hero.name)  # Salida: Anti-Mage
print(dota_hero.role)  # Salida: Carry
print(dota_hero.attack_type)  # Salida: Melee



## TKINTER .- LIBRERIA  DE PYTHON PARA LA CREACION DE  INTERFAZ GRAFICAS 
#Tkinter es una biblioteca de Python que se utiliza para crear interfaces gráficas de usuario 
# (GUI, por sus siglas en inglés). Es una herramienta muy útil para desarrollar aplicaciones con 
# una interfaz de usuario interactiva y atractiva. Tkinter se basa en la biblioteca Tcl/Tk, que es 
# una biblioteca de herramientas de desarrollo de software para crear interfaces gráficas de usuario. 

#Con Tkinter, puedes crear ventanas, botones, etiquetas, campos de entrada, menús y otros elementos de
# la interfaz de usuario. También puedes agregar imágenes y gráficos para hacer que tu aplicación sea más
# visualmente atractiva. Tkinter es fácil de aprender y usar, lo que lo hace ideal para principiantes en
# el desarrollo de aplicaciones de escritorio.