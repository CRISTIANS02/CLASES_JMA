

class Estudiante:
    nombre=input('Ingrese el nombre del estudiante: ')
    edad=input('Ingresela edad del estudiante del estudiante: ')
    carrera=input('Ingrese el nombre de la carrera: ')
    
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostr_Estudiante(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"

# Crear instancia de Estudiante
#estudiante1 = Estudiante("Juan", 20, "Ingeniería")

# Mostrar información del estudiante
print(Estudiante)