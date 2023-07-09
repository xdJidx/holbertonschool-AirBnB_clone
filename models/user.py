#!/usr/bin/python3
"""
Module User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ Initialize a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
