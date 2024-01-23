#!/usr/bin/env python3
"""
This module provides functionalities for user authentication.
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            bool: True if valid login, else False.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        # Directly use user.hashed_password without encoding
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with an email and password.
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
