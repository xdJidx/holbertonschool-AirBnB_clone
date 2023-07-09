#!/usr/bin/python3
"""
Consol of AirBnB clone
"""


import cmd
import sys
import models
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when End-Of-File character is encountered
        """
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print its id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            objects = models.storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            objects = models.storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in objects:
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = arg
            if class_name in models.__dict__ or class_name == "BaseModel":
                print([str(obj) for obj in objects.values() if
                       type(obj).__name__ == class_name])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                obj = obj_dict[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
