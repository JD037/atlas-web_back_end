#!/usr/bin/env python3
"""
BasicAuth module for handling basic authentication.
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64
from base64 import b64decode
import binascii


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization header.
        """
        if authorization_header is None or \
           not isinstance(authorization_header, str) or \
           not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 part of the Authorization header.
        """
        if base64_authorization_header is None or \
           not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            return decoded_bytes.decode('utf-8')
        except (ValueError, TypeError, base64.binascii.Error):
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or \
           not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        base64_header = self.extract_base64_authorization_header(auth_header)
        if base64_header is None:
            return None
        decoded_header = self.decode_base64_authorization_header(base64_header)
        if decoded_header is None:
            return None
        user_credentials = self.extract_user_credentials(decoded_header)
        if user_credentials is None:
            return None
        user = self.user_object_from_credentials(user_credentials[0],
                                                 user_credentials[1])
        return user
