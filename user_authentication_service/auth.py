#!/usr/bin/env python3
"""
This module provides functionalities for user authentication.
"""

import uuid
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

    def create_session(self, email: str) -> str:
        """
        Create a session ID for a user with the given email.

        Args:
            email (str): The email of the user.

        Returns:
            str: The session ID, or None if the user does not exist.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        user.session_id = session_id
        self._db._session.commit()

        return session_id


def _generate_uuid() -> str:
    """
    Generate a new UUID.

    Returns:
        str: A string representation of the newly generated UUID.
    """
    return str(uuid.uuid4())
