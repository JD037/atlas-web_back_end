#!/usr/bin/env python3
"""
Auth module for handling authentication.
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """
    Auth class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a particular path requires authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header value from the request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from the request.
        """
        return None
