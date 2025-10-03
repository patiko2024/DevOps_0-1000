# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Leer variables de entorno
    nombre = os.getenv('NOMBRE', 'Mundo')
    ruta_archivo = '/data/salida.txt'

    # Escribir en un archivo dentro del volumen montado
    with open(ruta_archivo, 'w') as f:
        f.write(f"Hola {nombre}!\n")

    return f"<h1>Hola {nombre} desde Docker!</h1><p>Archivo en {ruta_archivo}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
