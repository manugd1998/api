from flask import Flask, request, jsonify

app = Flask(__name__)

# Estado del solenoide (0 = cerrado, 1 = abierto)
estado_solenoide = 0

@app.route('/estado', methods=['GET'])
def obtener_estado():
    return jsonify({'estado': estado_solenoide})

@app.route('/control', methods=['POST'])
def cambiar_estado():
    global estado_solenoide
    datos = request.get_json()
    if 'estado' in datos and datos['estado'] in [0, 1]:
        estado_solenoide = datos['estado']
        return jsonify({'mensaje': 'Estado cambiado', 'estado': estado_solenoide})
    else:
        return jsonify({'error': 'Valor no válido, usa 0 o 1'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
