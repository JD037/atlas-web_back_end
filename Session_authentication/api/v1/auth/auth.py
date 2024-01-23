#!/usr/bin/env python3

""" Auth class """

from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class """

    def __init__(self):
        """ init """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth public method """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header public method"""
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user public method"""
        return None

    def session_cookie(self, request=None):
        """ session cookie public method"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
