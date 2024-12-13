# services/auth.py

import sqlite3

def get_connection():
    """Establece la conexión con la base de datos SQLite y asegura que la tabla users exista."""
    conn = sqlite3.connect("database.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

def authenticate(email, password):
    """Valida las credenciales del usuario en la base de datos SQLite."""
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


# services/auth.py

def register_user(email, password, name):
    """Registra un nuevo usuario en la base de datos SQLite."""
    try:
        conn = get_connection()
        conn.execute("INSERT INTO users (email, password, name) VALUES (?, ?, ?)", (email, password, name))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Este error ocurre si el correo ya existe en la base de datos
        return False
