from flask import Flask, jsonify, request

app = Flask(__name__)

estado_solenoide = {"solenoide": "OFF"}  # Estado inicial

@app.route('/estado-solenoide', methods=['GET'])
def obtener_estado():
    return jsonify(estado_solenoide)

@app.route('/cambiar-solenoide', methods=['POST'])
def cambiar_estado():
    global estado_solenoide
    datos = request.get_json()
    if "solenoide" in datos:
        estado_solenoide["solenoide"] = datos["solenoide"]
        return jsonify({"mensaje": "Estado actualizado"}), 200
    return jsonify({"error": "Parámetro faltante"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
