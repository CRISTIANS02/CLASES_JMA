class Estudiante:
    def __init__(self, estudiante_id, nombre, apellido, edad, carrera):
        self.estudiante_id = estudiante_id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        return f"ID: {self.estudiante_id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Carrera: {self.carrera}"

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []
        self.next_id = 1

    def agregar_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        edad = input("Ingrese la edad del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")
        estudiante = Estudiante(self.next_id, nombre, apellido, edad, carrera)
        self.estudiantes.append(estudiante)
        self.next_id += 1

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

    def actualizar_estudiante(self):
        estudiante_id = int(input("Ingrese el ID del estudiante a actualizar: "))
        for estudiante in self.estudiantes:
            if estudiante.estudiante_id == estudiante_id:
                nombre = input("Ingrese el nuevo nombre del estudiante: ")
                apellido = input("Ingrese el nuevo apellido del estudiante: ")
                edad = input("Ingrese la nueva edad del estudiante: ")
                carrera = input("Ingrese la nueva carrera del estudiante: ")
                estudiante.nombre = nombre
                estudiante.apellido = apellido
                estudiante.edad = edad
                estudiante.carrera = carrera
                print("Estudiante actualizado exitosamente.")
                return
        print("No se encontró ningún estudiante con el ID proporcionado.")

    def eliminar_estudiante(self):
        estudiante_id = int(input("Ingrese el ID del estudiante a eliminar: "))
        for estudiante in self.estudiantes:
            if estudiante.estudiante_id == estudiante_id:
                self.estudiantes.remove(estudiante)
                print("Estudiante eliminado exitosamente.")
                return
        print("No se encontró ningún estudiante con el ID proporcionado.")

# Crear instancia del gestor de estudiantes
gestor = GestorEstudiantes()

# Agregar estudiantes
gestor.agregar_estudiante()
gestor.agregar_estudiante()

# Mostrar estudiantes
print("Estudiantes registrados:")
gestor.mostrar_estudiantes()

# Actualizar estudiante
gestor.actualizar_estudiante()

# Mostrar estudiantes actualizados
print("Estudiantes actualizados:")
gestor.mostrar_estudiantes()

# Eliminar estudiante
gestor.eliminar_estudiante()

# Mostrar estudiantes restantes
print("Estudiantes restantes:")
gestor.mostrar_estudiantes()