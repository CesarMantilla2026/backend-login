from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# CORS configurado para escuchar a tu futuro Frontend
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Base de datos simulada en memoria
USUARIOS_DB = {
    "admin": "unfv2026"
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data:
        return jsonify({"status": "error", "message": "No se recibieron datos"}), 400
        
    username = data.get('username')
    password = data.get('password')
    
    if username in USUARIOS_DB and USUARIOS_DB[username] == password:
        return jsonify({
            "status": "success",
            "message": f"¡Autenticación exitosa! Bienvenido {username}.",
            "token": "token-falso-jwt-xyz789"
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Usuario o contraseña incorrectos"
        }), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)