#!/usr/bin/python3
""" Comment """


from base_model import BaseModel


class User(BaseModel):
    """ Initialize a user """

    """ Error Dictionary """
    error = {
        "email": "",
        "password": "",
        "first_name":
            "Your First Name must only contain alphabetic characters",
        "last_name":
            "Your Last Name must only contain alphabetic characters"
            }

    """
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    """
    def __init__(self, email, password, first_name, last_name):
        """ comment """

        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        """ Get/Set - the Email """
        return self.email

    @property
    def password(self):
        """ Get/Set - the Password """
        return self.password

    @property
    def first_name(self):
        """ Get/Set - the First Name """
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError(User.error["first_name"])
        self.first_name = value

    @property
    def last_name(self):
        """ Get/Set - the Last Name """
        return self.last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError((User.error["last_name"]))
        self.last_name = value
