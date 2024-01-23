#!/usr/bin/env python3
"""
SessionAuth class for managing user session authentication
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class that inherits from Auth.
    Manages sessions of users.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a user_id and returns the session ID.
        """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID.
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Retrieves the User instance for a request """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logs out.

        Args:
            request: The Flask request object from which the session ID will be retrieved.

        Returns:
            - True: If the session was successfully destroyed.
            - False: If the request is None, the session ID is not found in the request,
                    or the session ID is not linked to any User ID.

        This method removes the session ID from the user_id_by_session_id dictionary, effectively
        ending the user's session.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None or self.user_id_for_session_id(session_id) is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
