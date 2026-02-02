import sqlite3

# Nombre del archivo donde se guardarán los datos
DB_NAME = "emails.db"

def get_db_connection():
    """
    Crea la conexión con el archivo de base de datos.
    row_factory permite acceder a las columnas por nombre (ej: fila['email']).
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Esta función se ejecuta al arrancar.
    Crea la tabla 'users' si no existe todavía.
    """
    conn = get_db_connection()
    # SQL: Crea tabla con nombre (Clave primaria, no se repite) y email
    conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, email TEXT)')
    conn.commit() # Guardamos cambios
    conn.close()  # Cerramos conexión (importante para no bloquear el archivo)

def get_email_by_name(name):
    """
    Busca un usuario. Retorna el email (string) o None si no existe.
    """
    conn = get_db_connection()
    # Usamos '?' para evitar inyección SQL (seguridad básica)
    user = conn.execute('SELECT email FROM users WHERE name = ?', (name,)).fetchone()
    conn.close()
    
    if user:
        return user['email'] # Devolvemos solo el texto del mail
    return None

def add_user(name, email):
    """
    Intenta guardar un usuario nuevo.
    Retorna True si sale bien, False si el nombre ya existía.
    """
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        result = True
    except sqlite3.IntegrityError:
        # Este error salta automáticamente si el 'name' ya existe en la BD
        result = False 
    finally:
        conn.close() # Se ejecuta siempre, haya error o no
    
    return result