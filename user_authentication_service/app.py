#!/usr/bin/env python3
from flask import Flask, request, jsonify, abort, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Handle POST request for user login"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(401)  # Unauthorized if email or password missing

    if not AUTH.valid_login(email, password):
        abort(401)  # Unauthorized if invalid login

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logs out a user by destroying their session."""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)  # Forbidden if session ID is not present

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)  # Forbidden if no user found with the session ID

    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """GET /profile route to retrieve user profile."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)  # Forbidden if session ID is invalid or user does not exist

    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
