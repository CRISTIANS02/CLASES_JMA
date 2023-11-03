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
# 3.validar usuario y paswor
class usuario:
    def _init_(self, dni, nombre, f_nacimiento, edad,usuario, password):
        self.dni=dni
        self.nombre=nombre
        self.f_nacimiento=f_nacimiento
        self.edad=edad
        self.usuario=usuario
        self.password=password
        
    def mostrarUsuario(self,ide):
        respuesta=list(filter(lambda par:par['dni']==ide,usuarios))
        return f"""INFORMACION DEL USUARIO VALIDO"""
        {respuesta}
        
    def agregarEdad (self,clave,valor):
        for usuario in usuarios:
            if usuario['dni'] == self.dni:
                usuario[clave] = valor
                return 'Se actualizó.'
        return 'Usuario no encontrado.'

# verificar si usuario esta registrado o existe en mis registros
    def verificar_usuario(self, usuario_buscar):
        for usuario in usuarios:
            if usuario['usuario'] == usuario_buscar:
                return 'Usuario registrado.'
        return 'Usuario no encontrado en los registros.'

# validar usuario y password
    def validar_usuario_password(self, usuario_a_validar, password_a_validar):
        for usuario in usuarios:
            if usuario['usuario'] == usuario_a_validar and usuario['password'] == password_a_validar:
                return 'Usuario y contraseña válidos.'
        return 'Usuario o contraseña incorrectos.'

actu=Usuario(71440443,"cristian","02/54/2000",None,"","2000")
print(actu.agregar_edad("edad", 23))
print(actu.mostrar_usuario(71450443))
    
     