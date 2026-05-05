#!/usr/bin/env python3
"""Auth module for the API."""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns True
        if the path is not in the list of excluded paths."""
        return False

    def authorization_header(self, request=None) -> str:
        """Method that returns the value of the Authorization header."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that returns the current user."""
        return None
