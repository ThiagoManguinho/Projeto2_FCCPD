from flask import Flask, jsonify
import os
import redis
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'mydb')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASS = os.getenv('DB_PASS', 'password')

REDIS_HOST = os.getenv('REDIS_HOST', 'cache')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visitas (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        return "Tabela 'visitas' garantida."
    except Exception as e:
        return f"Falha ao inicializar o DB: {str(e)}"

@app.before_request
def setup():
    if not hasattr(app, 'db_initialized'):
        init_db()
        app.db_initialized = True

@app.route('/')
def hello():
    return "Hello from Docker Compose!"

@app.route('/db-data')
def db_data():
    """Insere um registro na tabela e lista todos os registros."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO visitas DEFAULT VALUES;")
        conn.commit()
        cur.execute("SELECT id, timestamp FROM visitas ORDER BY timestamp DESC;")
        registros = cur.fetchall()
        cur.close()
        conn.close()
        resultados = [{"id": r[0], "timestamp": str(r[1])} for r in registros]
        
        return jsonify({
            "status": "OK",
            "message": "Nova visita registrada com sucesso.",
            "total_visitas": len(resultados),
            "registros": resultados
        })
        
    except Exception as e:
        return jsonify({"status": "Error", "message": f"Falha ao acessar dados do DB: {str(e)}"}), 500

@app.route('/cache-test')
def cache_test():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        r.set('test_key', 'test_value')
        value = r.get('test_key')
        return f"Cache test successful! Value: {value}"
    except Exception as e:
        return f"Cache connection failed: {str(e)}"