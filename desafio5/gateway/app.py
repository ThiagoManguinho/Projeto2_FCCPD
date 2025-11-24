from flask import Flask, jsonify
import requests

app = Flask(__name__)

microservico1 = "http://usuarios:5001"
microservico2 = "http://pedidos:5002"

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        response = requests.get(f"{microservico1}/usuarios")

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"erro": "Usuários indisponível"}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro de conexão: {str(e)}"}), 500

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        response = requests.get(f"{microservico2}/pedidos")

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"erro": "Pedidos indisponível"}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro de conexão: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)