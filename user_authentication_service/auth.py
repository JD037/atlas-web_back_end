#!/usr/bin/env python3
"""
This module provides functionalities for user authentication.
"""

import bcrypt
from db import DB
from user import User  # Make sure this import is correct


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with an email and password.
        """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")

        hashed_password = _hash_password(password)
        return self._db.add_user(email, hashed_password)
