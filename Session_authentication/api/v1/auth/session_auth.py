#!/usr/bin/env python3
"""
This module contains the SessionAuth class
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth class that inherits from Auth.
    At the moment, this class is empty and serves as a placeholder
    for future implementation of session-based authentication.
    """

    def __init__(self):
        """
        Initialize the SessionAuth instance
        """
        super().__init__()
