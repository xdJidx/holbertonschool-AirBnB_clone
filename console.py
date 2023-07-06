#!/usr/bin/python3
"""
Consol of AirBnB clone
"""


import cmd
import sys
from datetime import datetime
import models

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
            """Create a new instance of BaseModel, save it, and print its id."""
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
            """Print the string representation of an instance."""
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
            """Delete an instance based on the class name and id."""
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
                try:
                    class_name = arg
                    print([str(obj) for obj in objects.values() if type(obj).__name__ == class_name])
                except NameError:
                    print("** class doesn't exist **")

    def do_update(self, arg):
            """Update an instance based on the class name and id."""
            if not arg:
                print("** class name missing **")
                return
            try:
                args = arg.split()
                class_name = args[0]
                instance_id = args[1]
                attribute_name = args[2]
                attribute_value = args[3]

                objects = models.storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in objects:
                    instance = objects[key]
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
            except ValueError:
                print("** attribute name missing **")
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()