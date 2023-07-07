#!/usr/bin/python3
"""
Contains FileStorage class
"""


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes them back to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with
        key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file path
        """
        jsonObject = {}
        for key in self.__objects:
            jsonObject[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(jsonObject, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                jl = json.load(f)
            for key in jl:
                self.__objects[key] = classes[jl[key]["__class__"]](**jl[key])
        except FileNotFoundError:
            pass

    def serialize_user(self, user):
        return json.dumps(user.__dict__)

    def deserialize_user(self, json_data):
        user_data = json.loads(json_data)
        user = User()
        user.__dict__.update(user_data)
        return user
