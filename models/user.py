#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Return a list of all User instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("User."):
                result.append(str(instance))

        return result

    @classmethod
    def count(cls):
        """Count all User instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("User."):
                result.append(str(instance))

        print(len(result))

    @classmethod
    def show(cls, id=None):
        """Return the User instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        instance = FileStorage.get_by_id(cls, "User", id)

        if instance is None:
            print("** no instance found **")
        else:
            print(f'{instance}')

    @classmethod
    def destroy(cls, id=None):
        """Destroy the User instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        instance = FileStorage.get_by_id(cls, "User", id)

        if instance is None:
            print("** no instance found **")
        else:
            FileStorage.destroy(cls, "User", id)

    @classmethod
    def update(cls, id=None, args=None):
        """Update the User instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        if args is None:
            print("** arguments are missing **")
            return

        instance = FileStorage.get_by_id(cls, "User", id)

        if not instance:
            print("** no instance found **")
            return

        else:
            FileStorage.update(cls, "User", id, args)
