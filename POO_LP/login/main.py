# importar mi base de datos
#from bdd import * # la variable usuarios de mi bd estara disponible en este archivo
#crear clase para usurio
# esta clase tendra los siguientes metodos
#actualizar edad del usuario
#verificar si el usuario esta registrado o existe en mis registros
# validar usuario y pasword

# crear una lista de 5 objetos donde cada objeto tendra los siguientes 
# datos de una persona. nombre,edad,f_nacimiento,dni,usuario,password
# usuarios[{
#      'dni': 12345678,
#      'nombre': 'Moises',
#      'f_nacimiento': '28/10/2023', 
#      'edad': '',
#      'usuario': 71450443,
#      'password': '71450443'
#      }]

# 1.actualizar edad del usuario
# 2.verificar si el usuario esta registrado o existe en mis registros
# 3.validar usuario y pasword
from bdd import * # la variable usuario estara disponible en este archivo

class Usuario:

    # def __init__(self,dni,nombre, fecha_nacimiento,edad,usuario,password):
    #     self.dni=dni
    #     self.nombre=nombre
    #     self.fecha_nacimiento=fecha_nacimiento
    #     self.edad=edad
    #     self.usuario=usuario
    #     self.password=password
    
    def edad(self):
        pass #hoy=
    
    def actualizar_edad(self,clave,valor):
        for user in usuarios:
            if user['dni']== self.dni:
                user[clave]= valor
        return 'actualizado'
        

    def ver_usuario(self,dato):
        g=list(filter(lambda par:par['dni']==dato,usuarios))
        return f'''Ainformacion por dni {dato}
        ...
        {g}'''
    def verificar_user(self,usuario_buscar):
        for user in usuarios:
            if user['usuario'] == usuario_buscar:
                return 'Usuario si existe.'
        return 'Usuario resgistrado.'

    def validar(self, usuario, password):
        for user in usuarios:
            if user['usuario']==usuario:
                if user['password']==password:
                    return 'Datos validados'
        return 'Datos invalidos'
        
        pass
b=Usuario(75248698,'Maria','10/02/2005','','maria@gmail.com','m1234')
# metodo que sabiendo la fecha de nacimiento me va generar la edad
# crear clase para usuario, debera tener los siguientes metodos
# actualizar edad del usuario
# verificar si usuario esta registrado o existe en mis registros
# validar usuario y password

print(b.actualizar_edad('edad','17'))
print(b.actualizar_edad(75248698,'edad',''))
print(b.validar('maria@gmail.com','m1234'))
print(b.ver_usuario(75248698))
print(b.verificar_user('maria@gmail.com'))