#!/usr/bin/python3
"""
Module base_model
Contains BaseModel class
"""


import uuid
from datetime import datetime
import models
fmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Represent a class BaseModel that defines
    all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes data
        """
        if kwargs:
            for key, value in kwargs.items():
                if (hasattr(self, "created_at") and
                   type(self.created_at) is str):
                    self.created_at = datetime.strptime
                    (kwargs["created_at"], fmt)
                if (hasattr(self, "updated_at") and
                   type(self.updated_at) is str):
                    self.updated_at = datetime.strptime
                    (kwargs["updated_at"], fmt)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns:
        a readable string representation of an instance
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates public attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dict with all keys/values of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict.update([("__class__", self.__class__.__name__)])
        for key, value in dict.items():
            if key == "created_at":
                dict.update([(key, value.isoformat())])
            elif key == "updated_at":
                dict.update([(key, value.isoformat())])
            else:
                dict.updated([(key, value)])
        return dict
