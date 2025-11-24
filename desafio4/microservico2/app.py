from flask import Flask, jsonify
import requests
import datetime

app = Flask(__name__)

microservico1 = "http://usuarios:5001"

@app.route('/info-usuarios', methods=['GET'])
def get_info_usuarios():
    try:
        resposta = requests.get(f"{microservico1}/usuarios")
        
        if resposta.status_code == 200:
            usuarios = resposta.json()
            usuarios_processados = []
            for usuario in usuarios:
                data_criacao = usuario['data_criacao']                
                usuarios_processados.append({
                    "id": usuario['id'],
                    "mensagem": f"Usuario {usuario['nome']} ativo desde {data_criacao}"
                })
            return jsonify(usuarios_processados)
        else:
            return jsonify({"erro": "Falha ao consultar serviço de usuários"}), 500
            
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro de conexão: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)