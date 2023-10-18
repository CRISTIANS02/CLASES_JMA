class Estudiante:
    def __init__(self,id_estudiante, nombre, apellido, edad, carrera):
        self.id_estudiante=id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        return f"ID: {self.id_estudiante}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Carrera: {self.carrera}"

class Estudiantes:
    def __init__(self):
        self.estudiantes = []
        self.next_id = 1

print(Estudiante)