from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def conectar():
    """Establece la conexión a la base de datos MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mandrake99",
        database="clientes_bayma"
    )

@app.route('/webhook', methods=['POST'])#Crear un endpoint para recibir datos
def webhook():
    data = request.get_json()

    if 'evento' not in data or 'mensaje' not in data or 'timestamp' not in data:
        return jsonify({'status': 'error', 'mensaje': 'Faltan campos'}), 400 #Validar los campos requeridos


    try:
        connection = conectar()
        cursor = connection.cursor()

        query = "INSERT INTO logs (evento, mensaje, timestamp) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['evento'], data['mensaje'], data['timestamp']))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            'status': 'ok',
            'recibido': data
        })

    except Exception as e:
        return jsonify({'status': 'error', 'mensaje': str(e)}), 500 #Confirma que se ha insertado correctamente

if __name__ == '__main__':
    app.run(debug=True)
