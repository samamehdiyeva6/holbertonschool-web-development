#!/usr/bin/env python3
"""Auth module for the API."""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns True
        if the path is not in the list of excluded paths."""
        if (
            path is None
            or excluded_paths is None
            or excluded_paths == []
        ):
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if not excluded.endswith('/'):
                excluded += '/'
            if path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Method that returns the value of the Authorization header."""
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')


    def current_user(self, request=None) -> TypeVar('User'):
        """Method that returns the current user."""
        return None
