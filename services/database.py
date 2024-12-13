def save_defect(fecha, linea_produccion, producto, descripcion, causa):
    # Replace with actual database logic
    try:
        # Simulate saving to database
        print(f"Saving defect: {fecha}, {linea_produccion}, {producto}, {descripcion}, {causa}")
        return True
    except Exception as e:
        print(f"Error saving defect: {e}")
        return False

# Crear la base de datos y la tabla de usuarios
import sqlite3

def create_users_table():
    conn = sqlite3.connect("database.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Ejecuta esta función una vez para crear la tabla
create_users_table()
