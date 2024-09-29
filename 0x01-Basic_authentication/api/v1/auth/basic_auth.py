#!/usr/bin/env python3
""" import modules """
from .auth import Auth
from flask import request
from typing import List, TypeVar
from os import getenv


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header: str
                                            ) -> str:
        """ returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64_authorization_header.decode('utf-8').decode('base64')
        except Exception:
            return None
