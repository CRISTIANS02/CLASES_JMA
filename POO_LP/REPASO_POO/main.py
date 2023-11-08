# REPASO PARA  DE POGRAMACION ORIENTADA A OBJETOS
from rich import *
class Mascota:
    def __init__ (self):
        self.nombre=None
        self.edad=None
        self.tipo_animal=None
    def hablar(self,sonido):
        return sonido
    def datos_mascota(self,nombre,edad,tipo_animal):
        self.nombre=nombre
        self.edad=edad
        self.tipo_animal=tipo_animal
# REPASO PARA  DE POGRAMACION ORIENTADA A OBJETOS
class Perro(Mascota):
    def atacar(self):
        return "ladra y muerde"
    
class gato(Mascota):
    pass

perro_body=Perro()
perro_body.datos_mascota("boby",14,"perro")
print(f"[bold blue]"+ perro_body.hablar('guau guau'))
print("[bold blue]"+ perro_body.tacar())
print("[bold blue]"+ perro_body.nombre+" " + perro_body.tipo_animal)




# # ejercicio 1

# # REPASO PARA  DE POGRAMACION ORIENTADA A OBJETOS
# from rich import *
# class Persona:
#     def __init_(self,nombre:str,edad:int,sexo:str):
#         self.nombre=None
#         self.edad=None
#         self.sexo=sexo
#     def comen(self,plato_faborito:str):
#         return f"yo {self.nombre}estoy comiendo mi {plato_faborito}"
#     def cagan (self):
#         return " pipi popo"
    
# class Estudiante (Persona):
#     def __init__(self,nombre:str,edad:int,sexo:str,carrera_profecional:str):
#         super().__init__(nombre,edad,sexo)
#         self.carrera_profecional=carrera_profecional
#     def estudiar(self):
#         return" estoy estudiando POO"
        
# class Trabajador (Persona):
#     def __init__(self,nombre:str,edad:int,sexo:str,profecion:str):
#         super().__init__(nombre,edad,sexo)
#         self.profecion=profecion
#     def trabajar(self):
        