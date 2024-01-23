#!/usr/bin/env python3
""" Module for Session Authentication views """

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handles POST request for user login session.

    - Retrieves email and password from the request form.
    - Validates the presence of email and password.
    - Searches for the user by email.
    - Validates the user's password.
    - Creates a new session for the user.
    - Sets a cookie with the session ID in the response.
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    DELETE /api/v1/auth_session/logout
    Description:
        Logs out a user by destroying their session.
        If the session ID is not found or invalid, returns a 404 error.
    Returns:
        - Empty JSON dictionary with the status code 200 if the session was successfully destroyed.
        - 404 error if the session ID does not exist or is invalid.
    """
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
