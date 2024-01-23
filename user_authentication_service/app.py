#!/usr/bin/env python3
from flask import Flask, request, jsonify, abort
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Handle POST request for user registration"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(400)  # Bad request if email or password missing

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:  # User already exists
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
