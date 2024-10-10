import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                dni TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                estado TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def create_user(self, dni, nombre, apellido, estado):
        self.cursor.execute('''
            INSERT INTO usuarios (dni, nombre, apellido, estado)
            VALUES (?, ?, ?, ?)
        ''', (dni, nombre, apellido, estado))
        self.connection.commit()

    def read_user(self, dni):
        self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
        return self.cursor.fetchone()

    def update_user(self, dni, nombre, apellido, estado):
        self.cursor.execute('''
            UPDATE usuarios
            SET nombre = ?, apellido = ?, estado = ?
            WHERE dni = ?
        ''', (nombre, apellido, estado, dni))
        self.connection.commit()

    def delete_user(self, dni):
        self.cursor.execute('DELETE FROM usuarios WHERE dni = ?', (dni,))
        self.connection.commit()

    def close(self):
        self.connection.close()
