#!/usr/bin/env python3
"""
This module provides a function to hash passwords using bcrypt.
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
