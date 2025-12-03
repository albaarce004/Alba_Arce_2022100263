from flask import Flask, render_template, request, redirect, url_for
from db_connection import get_db_connection  # <-- esto debe coincidir con el nombre de la función

app = Flask(__name__)


get_connection = get_db_connection


# LISTA DE LOTES
@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lotes")
    lotes = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("index.html", lotes=lotes)


# DETALLE DE LOTE
@app.route('/lote/<int:id>')
def detalle_lote(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lotes WHERE id = %s", (id,))
    lote = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template("detalle.html", lote=lote)


# FORMULARIO DE CONTACTO
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        celular = request.form['celular']
        horario = request.form['horario']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contactos (nombre, apellido, correo, celular, horario_llamada) VALUES (%s, %s, %s, %s, %s)",
            (nombre, apellido, correo, celular, horario)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("index"))

    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
