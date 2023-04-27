#!/usr/bin/env python3
"""
Hash passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Return hashed password as a string. """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Tkes two args and returns a boolean. """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
