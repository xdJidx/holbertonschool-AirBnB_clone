#!/usr/bin/python3
""" Comment """


from models.base_model import BaseModel


class User(BaseModel):
    """ Initialize a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
