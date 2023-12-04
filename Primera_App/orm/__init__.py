import sqlite3
import json

class SQLiteORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.conn.cursor()

    def crear_tabla(self, table_definition):
        # Crea una tabla a partir de la definición en formato JSON
        for table_name, columns in table_definition.items():
            columns_str = ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns_str})"
            self.cursor.execute(query)
        self.conn.commit()

    def insertarUno(self, table_name, data):
        # Inserta un nuevo registro en la tabla
        columns = ', '.join(data.keys())
        values = ', '.join([f":{key}" for key in data.keys()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(query, data)
        self.conn.commit()

    def insertarVarios(self, table_name, data):
        # Inserta un nuevo registro en la tabla desde una array de objetos
        for d in data:
            columns = ', '.join(d.keys())
            values = ', '.join([f":{key}" for key in d.keys()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.executemany(query, data)
        self.conn.commit()

    def actualizar(self, table_name, data, where):
        # Actualiza registros en la tabla
        set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
        self.cursor.execute(query, data)
        self.conn.commit()

    def eliminar(self, table_name, where):
        # Elimina registros de la tabla
        query = f"DELETE FROM {table_name} WHERE {where}"
        self.cursor.execute(query)
        self.conn.commit()

    def mostrar(self, table_name, where=None, type=None):
        # Realiza una consulta SELECT
        query = f"SELECT * FROM {table_name}"
        if where:
            query += f" WHERE {where}"

        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if type == "objeto":
            columns = [desc[0] for desc in self.cursor.description]

            results = []
            for row in rows:
                result_dict = dict(zip(columns, row))
                results.append(result_dict)
            formateo_json=json.dumps(results, indent=4)
            return formateo_json
        else:
            return rows
    def cerrar(self):
        self.conn.close()
