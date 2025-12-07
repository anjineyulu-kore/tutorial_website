from flask import Flask, request, jsonify, send_from_directory
import os
import json
from datetime import datetime
from uuid import uuid4

# Simple Flask server to handle registration and admin approvals
# Usage: python server.py

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
ADMIN_TOKEN = os.environ.get('TA_ADMIN_TOKEN', 'admin123')  # change via environment

app = Flask(__name__, static_folder='')

# Ensure data directory and file exist
os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, indent=2)


def load_users():
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def require_admin(req):
    token = req.headers.get('X-Admin-Token') or req.args.get('token')
    return token == ADMIN_TOKEN


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Admin-Token'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    return response


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    course = data.get('course', 'general')

    if not name or not email:
        return jsonify({'error': 'name and email are required'}), 400

    users = load_users()
    user_id = str(uuid4())
    user = {
        'id': user_id,
        'name': name,
        'email': email,
        'course': course,
        'status': 'pending',
        'registered_at': datetime.utcnow().isoformat() + 'Z'
    }
    users.append(user)
    save_users(users)

    return jsonify({'message': 'registered', 'id': user_id}), 201


@app.route('/api/users', methods=['GET'])
def list_users():
    if not require_admin(request):
        return jsonify({'error': 'admin token required'}), 401
    users = load_users()
    return jsonify(users)


@app.route('/api/users/<user_id>/approve', methods=['POST'])
def approve_user(user_id):
    if not require_admin(request):
        return jsonify({'error': 'admin token required'}), 401
    users = load_users()
    for u in users:
        if u['id'] == user_id:
            u['status'] = 'approved'
            u['approved_at'] = datetime.utcnow().isoformat() + 'Z'
            save_users(users)
            return jsonify({'message': 'approved', 'id': user_id})
    return jsonify({'error': 'user not found'}), 404


@app.route('/api/users/<user_id>/reject', methods=['POST'])
def reject_user(user_id):
    if not require_admin(request):
        return jsonify({'error': 'admin token required'}), 401
    users = load_users()
    for u in users:
        if u['id'] == user_id:
            u['status'] = 'rejected'
            u['rejected_at'] = datetime.utcnow().isoformat() + 'Z'
            save_users(users)
            return jsonify({'message': 'rejected', 'id': user_id})
    return jsonify({'error': 'user not found'}), 404


@app.route('/data/users.json', methods=['GET'])
def serve_users_file():
    # serve file for convenience (not secure) - admin token required
    if not require_admin(request):
        return jsonify({'error': 'admin token required'}), 401
    return send_from_directory(DATA_DIR, 'users.json')


@app.route('/')
def root():
    return "Test Automation Hub API - use /api/register to sign up"


if __name__ == '__main__':
    print('Starting server on http://127.0.0.1:5000')
    print('Admin token:', ADMIN_TOKEN)
    app.run(host='127.0.0.1', port=5000, debug=True)
