#!/usr/bin/env python3
"""
Module auth
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """ Class authentication. """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required. """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Get auth header from request. """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get current user from request. """
        return None
