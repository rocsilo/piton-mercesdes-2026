from flask import Flask, render_template, request
import maildb as db  # Importamos nuestro archivo maildb.py

app = Flask(__name__)

# Al iniciar la app, nos aseguramos de que la base de datos exista
db.init_db()

# --- RUTA PRINCIPAL (BUSCADOR) ---
@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializamos variables vacías
    result_email = None
    error = None
    
    # Si el usuario ha pulsado el botón "Cercar" (Método POST)
    if request.method == 'POST':
        name = request.form['name'] # Cogemos el dato del input HTML
        
        # Llamamos a la función de nuestro módulo de BD
        email = db.get_email_by_name(name)
        
        if email:
            result_email = email # ¡Encontrado!
        else:
            error = f"L'usuari '{name}' no existeix a la base de dades."

    # --- CAMBIO IMPORTANTE AQUÍ ABAJO ---
    # Usamos 'get.html' porque así es como se llama tu archivo en la carpeta templates
    return render_template('get.html', result_email=result_email, error=error)

# --- RUTA AÑADIR (NUEVO USUARIO) ---
@app.route('/add', methods=['GET', 'POST'])
def add():
    msg = None
    msg_type = None # Esto controlará el color de la alerta (verde/rojo)
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # Intentamos guardar. Si devuelve True, es éxito.
        if db.add_user(name, email):
            msg = f"Usuari '{name}' desat correctament!"
            msg_type = "success" # Clase CSS de Bootstrap para verde
        else:
            msg = f"Error: L'usuari '{name}' ja existeix."
            msg_type = "danger"  # Clase CSS de Bootstrap para rojo

    return render_template('add.html', msg=msg, msg_type=msg_type)

if __name__ == '__main__':
    # host='0.0.0.0' es OBLIGATORIO para que funcione dentro de Docker
    app.run(host='0.0.0.0', port=5000, debug=True)