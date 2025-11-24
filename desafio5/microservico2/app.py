from flask import Flask, jsonify

app = Flask(__name__)

pedidos = [
    {"id": 1, "usuario_id": 1, "produto": "Notebook", "valor": 2500.00},
    {"id": 2, "usuario_id": 2, "produto": "Celular", "valor": 1200.00},
    {"id": 3, "usuario_id": 1, "produto": "Tablet", "valor": 800.00},
    {"id": 4, "usuario_id": 3, "produto": "mouse", "valor": 600.00}
]

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    return jsonify(pedidos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)