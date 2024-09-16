#!/usr/bin/env python3


"""importing the hashlib module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a hashed password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Returns a boolean """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
