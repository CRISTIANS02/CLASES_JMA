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

#1
import datetime
import random

usuarios = []

for i in range(5):
  usuarios.append({
    'dni': random.randint(10000000,99999999),
    'nombre': 'Usuario ' + str(i+1),
    'f_nacimiento': str(datetime.date(random.randint(1950,2005), random.randint(1,12), random.randint(1,28))),
    'edad': '',
    'usuario': random.randint(100000,999999),
    'password': 'password'+str(i)
  })

print(usuarios)

# 1. Actualizar edades
from datetime import datetime
for usuario in usuarios:
  fecha_nac = datetime.strptime(usuario['f_nacimiento'], '%Y-%m-%d')
  usuario['edad'] = int((datetime.now() - fecha_nac).days / 365) 

print(usuarios)

# 2. Verificar si usuario existe
dni_buscar = usuarios[3]['dni']  
print(any(u['dni'] == dni_buscar for u in usuarios))

# 3. Validar usuario y contraseña
user_validar = usuarios[4]['usuario']
pass_validar = usuarios[4]['password']
print(any(u['usuario'] == user_validar and u['password'] == pass_validar for u in usuarios))







#2





# # actualizacion de edad

# from datetime import *
# from bdd import *
# for usuario in usuarios:
#   fecha_nac = datetime.strptime(usuario['f_nacimiento'], '%d/%m/%Y')
#   usuario['edad'] = int((datetime.now() - fecha_nac).days / 365)

# print(usuarios)

# # Verificar usuario existente
# dni_buscar = 12345678
# print(any(u['dni'] == dni_buscar for u in usuarios))

# # Validar usuario y contraseña
# dni_validar = 98765432 
# password_validar = 'qwerty123'
# #print(any(u['dni'] == dni_validar and u['password'] == password_validar for u in usuarios))
