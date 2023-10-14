# #crear un objeto haciendo uso de la POO crear un objeto para cda edentidad celular
# class Celular:
#     def __init__(self, marca, modelo, color, capacidad_almacenamiento):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.capacidad_almacenamiento = capacidad_almacenamiento

#     def mostrar_informacion(self):
#         print("Información del Celular:")
#         print("Marca:", self.marca)
#         print("Modelo:", self.modelo)
#         print("Color:", self.color)
#         print("Capacidad de Almacenamiento:", self.capacidad_almacenamiento)


# # Crear una instancia de la clase Celular
# celular1 = Celular("Samsung", "Galaxy S20", "Negro", "128GB")

# # Mostrar la información del celular
# celular1.mostrar_informacion()



# # haciendo uso de la POO crear un objeto para la edentidad vehiculo
# class Vehiculo:
#     def __init__(self, marca, modelo, año):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año

#     def mostrar_info(self):
#         print(f"Marca: {self.marca}")
#         print(f"Modelo: {self.modelo}")
#         print(f"Año: {self.año}")

# coche = Vehiculo("Toyota", "Corolla", 2021)
# coche.mostrar_info()


# # haciendo uso de la POO crear un objeto para la edintidad avion
# class Avion:
#     def __init__(self, modelo, capacidad, velocidad_maxima):
#         self.modelo = modelo
#         self.capacidad = capacidad
#         self.velocidad_maxima = velocidad_maxima

#     def mostrar_informacion(self):
#         print(f"Modelo: {self.modelo}")
#         print(f"Capacidad: {self.capacidad}")
#         print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")

# avion1 = Avion("Boeing 747", 416, 988)
# avion1.mostrar_informacion()




# # haciendo uso de la POO crear un objeto para la edintidad dota 2

# class Dota2:
#     def __init__(self, hero, role, attack_type):
#         self.hero = hero
#         self.role = role
#         self.attack_type = attack_type

#     def display_hero_info(self):
#         print("Héroe:", self.hero)
#         print("Rol:", self.role)
#         print("Tipo de Ataque:", self.attack_type)

#     def calculate_damage(self, base_damage, attack_speed):
#         total_damage = base_damage * attack_speed
#         return total_damage


# ##Crear una instancia de la clase Dota2
# dota_hero = Dota2("Juggernaut", "Carry", "Melee")

# ##Mostrar la información del héroe
# dota_hero.display_hero_info()

# #Calcular el daño con 50 de daño base y 1.5 de velocidad de ataque
# daño_total = dota_hero.calculate_damage(50, 1.5)
# print("Daño Total:", daño_total)


# # haciendo uso de la POO crear un objeto para  una pc

# class PC:
#     def __init__(self, marca, modelo, procesador, ram, almacenamiento):
#         self.marca = marca
#         self.modelo = modelo
#         self.procesador = procesador
#         self.ram = ram
#         self.almacenamiento = almacenamiento
#         self.encendida = True

#     def encender(self):
#         if self.encendida:
#             print("La PC ya está encendida.")
#         else:
#             self.encendida = True
#             print(f"La PC {self.marca} {self.modelo} está encendida.")

#     def apagar(self):
#         if not self.encendida:
#             print("La PC ya está apagada.")
#         else:
#             self.encendida = False
#             print(f"La PC {self.marca} {self.modelo} está apagada.")

#     def mostrar_especificaciones(self):
#         print("Especificaciones de la PC:")
#         print("Marca:", self.marca)
#         print("Modelo:", self.modelo)
#         print("Procesador:", self.procesador)
#         print("RAM:", self.ram)
#         print("Almacenamiento:", self.almacenamiento)


# # Crear una instancia de la clase PC
# pc1 = PC("Dell", "Inspiron", "Intel Core i5", "8GB", "256GB SSD")

# # Encender la PC
# pc1.encender()

# # Mostrar las especificaciones de la PC
# pc1.mostrar_especificaciones()

# # Apagar la PC
# pc1.apagar()




# # haciendo uso de la POO crear un objeto para una impresora
# class Impresora:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#         self.imprimiendo =True

#     def imprimir_documento(self, documento):
#         if self.imprimiendo:
#             print("Error: La impresora ya está imprimiendo.")
#         else:
#             self.imprimiendo = True
#             print(f"Imprimiendo documento '{documento}' en la impresora {self.marca} {self.modelo}...")
#             # Lógica para imprimir el documento
#             self.imprimiendo = False
#             print("Impresión completada.")

#     def verificar_estado(self):
#         if self.imprimiendo:
#             print("La impresora está ocupada.")
#         else:
#             print("La impresora está lista para imprimir.")


# # Crear una instancia de la clase Impresora
# impresora1 = Impresora("HP", "Deskjet 1234")

# # Imprimir un documento
# impresora1.imprimir_documento("Documento1.pdf")

# # Verificar el estado de la impresora
# impresora1.verificar_estado()




# # # haciendo uso de la POO crear un objeto para emitir un fctura
# class Printer:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.is_printing =False

#     def print_documento(self, documento):
#         if self.is_printing:
#             print("peligro !CTM¡¡  : La impresora ya está imprimiendo.")
#         else:
#             self.is_printing = True
#             print(f"Imprimiendo documento '{documento}' en la impresora {self.brand} {self.model}...")
            
#             # Lógica para la imprecion del documento
            
#             self.is_printing = False
#             print("Impresión completada.")

#     def check_status(self):
#         if self.is_printing:
#             print("La impresora está ocupada jilipollas.")
#         else:
#             print("La impresora está lista para imprimir Princeso.")


# # Crear una instancia de la clase Printer
# printer1 = Printer("HP", "Deskjet 1234")

# # Imprimir un documento
# printer1.print_documento("FACTURA COMPRA 1.pdf")

# # Verificar el estado de la impresora
# printer1.check_status()


#clase 10/10/2023


#1. CREAR UN OBJETO LAPTOP CON 2 ATRIBUTOS DE CLASE Y 5 ATRIBUTOS DE INSTANCIA,
# DEBERA TENER HASTA 3 FUNCIONALIDADES COMO MINIMO.
#CREAR TRES OBJETOS INSTANCIA DE CLASES DISTINTOS
## OJO: Solo utilizar lo utilizado en clase 10/10/2023

# LAPTOP HP
# class Laptop:
   
#     tcladoNumerico=True
#     tipo='pc portatil'
   
#     def __init__(self,marca,modelo,serie,S_Opeativo,ram):
#         self.marca=marca  
#         self.modelo=modelo
#         self.serie=serie
#         self.S_Operativo=S_Opeativo
#         self.ram=ram
    
#     funciaonalidades
#     def  info(self):
#         respuest=f'''
#         ::::::::::::::::::::::::::::::::::::::::::::::
#         tipo:{self.tipo}
#         marca | modelo | serie | S_Operativo | ram
#         {self.marca}{self.modelo}{self.serie}{self.S_Operativo}{self.ram}
        
#         ::::::::::::::::::::::::::::::::::::::::::::::
        
#         '''
#         return respuest
    
    
    # def encender(self):
#REAR UNA CLASE DEPUESTO DE  MERCADO QUE TENGA UN ATRIBUTO DE CLASE 5 ATRUBUTOS DE INSTANCIA Y 5 FUNCIONALIDADES
#DEBERA CREAR 4 INSTANCIA DE LA CLASE MERCADO

class MarketPuesto:
    class_attribute = "Some value"  # Class attribute

    def __init__(self, attribute1, attribute2, attribute3, attribute4, attribute5):
        self.attribute1 = attribute1  # Instance attribute 1
        self.attribute2 = attribute2  # Instance attribute 2
        self.attribute3 = attribute3  # Instance attribute 3
        self.attribute4 = attribute4  # Instance attribute 4
        self.attribute5 = attribute5  # Instance attribute 5

    def functionality1(self):
        # Functionality 1
        pass

    def functionality2(self):
        # Functionality 2
        pass

    def functionality3(self):
        # Functionality 3
        pass

    def functionality4(self):
        # Functionality 4
        pass

    def functionality5(self):
        # Functionality 5
        pass

# Creating instances of the MarketPuesto class
market1 = MarketPuesto("Value1", "Value2", "Value3", "Value4", "Value5")
market2 = MarketPuesto("Value6", "Value7", "Value8", "Value9", "Value10")
market3 = MarketPuesto("Value11", "Value12", "Value13", "Value14", "Value15")
market4 = MarketPuesto("Value16", "Value17", "Value18", "Value19", "Value20")