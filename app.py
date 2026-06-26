from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# 🔗 Conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="libreria"
)

cursor = db.cursor()

# 🏠 Mostrar formulario
@app.route("/")
def home():
    return render_template("index.html")


# 🧾 Registrar usuario
@app.route("/registro", methods=["POST"])
def registro():
    nombre = request.form["nombre"]
    usuario = request.form["usuario"]
    password = request.form["password"]

    sql = "INSERT INTO usuarios (nombre, usuario, password) VALUES (%s, %s, %s)"
    valores = (nombre, usuario, password)

    cursor.execute(sql, valores)
    db.commit()

    return "Usuario registrado correctamente"


if __name__ == "__main__":
    app.run(debug=True)