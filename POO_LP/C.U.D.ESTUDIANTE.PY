# formas normales  ( normalizacion de  de base de datos )
Alumnos=[
    {
        'id':1,
        'nombre':'cristian',
        'apellido':'Poma Ramos',
        'dni':71450443,
        'edad':'20',
        'fecha_nacimineto':'02-05-2000',
     }
]
#caso de uso
class Alumno:
    # Atributos de instancia
    def __init__(self,nombre,apellido,dni,edad,fecha_nacimiento):
    
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.edad=edad
        self.fecha_nacimiento=fecha_nacimiento
       
    
    # creacion de metodos
    def mostrar_Alumnos(self):
        mensaje=f"""
        tienes {len(Alumnos)} Alumnos
        los Alumnos son:
        {Alumnos}
        """
        return mensaje
    def registrar_alumno(self):
        nuevo_id=len(Alumnos)+1
        Alumno_nuevo={
            'id:nuevo_id',
            'nombre:self_nombre',
            'apellido:self_apellido'
            'dni:self_dni',
            'edad:self_edad',
            'fecha de nacimiento:self_fecha_de_nacimiento'
           
            
        }
        
        registro_Alumno=Alumnos.append(Alumno_nuevo)
        return f" El sigiente Alumno se registro exitosamente(producto_nuevo)"
       
    def mostrar_alumno(self,id):
        Alumno_buscar=Alumnos(id-1)
        return Alumno_buscar
    
    def eliminar_alumno(self,id):
        Alumno_eliminar=Alumnos.pop(id-1)
        return  f"El sigiente Alumno fue eliminado{Alumno_eliminar}"
    
    
    def actualizar_Alumno(self,id):
     pass
    
alumn=Alumno('jose','ramos','785694226','20','12-12-2001')
print=(alumn.registar_alumno())
print=(alumn.mostrar_alumno())
#print=(alumn.registar_alumno())
#print=(alumn.eliminar_alumno())
print=(alumn.mostrar_alumno())

