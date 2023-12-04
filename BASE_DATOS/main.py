import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('database.sqlite')

# Crear una tabla
c = conn.cursor()
c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')

# Cerrar la conexión
conn.close()