#!/usr/bin/python3
"""
User class module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Define user information
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
