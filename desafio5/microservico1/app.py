from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Thiago Sousa", "data_criacao": "2005-02-23"},
    {"id": 2, "nome": "Maria Eduarda", "data_criacao": "2004-08-20"},
    {"id": 3, "nome": "Renata", "data_criacao": "1969-05-10"}
]

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)