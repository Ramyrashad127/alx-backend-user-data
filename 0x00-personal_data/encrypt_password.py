#!/usr/bin/env python3


"""importing the hashlib module"""
import bcrypt


def hash_password(password: str) -> str:
    """ Returns a hashed password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
