#!/usr/bin/env python3
""" import modules """
from .auth import Auth
from flask import request
from typing import List, TypeVar
from os import getenv


class BasicAuth(Auth):
    """ BasicAuth class
    """
    pass
