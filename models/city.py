#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Return a list of all City instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("City."):
                result.append(str(instance))

        print(result)

    @classmethod
    def count(cls):
        """Count all City instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("City."):
                result.append(str(instance))

        print(len(result))

    @classmethod
    def show(cls, id=None):
        """Return the City instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        instance = FileStorage.get_by_id(cls, "City", id)

        if instance is None:
            print("** no instance found **")
        else:
            print(f'{instance}')

    @classmethod
    def destroy(cls, id=None):
        """Destroy the City instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        instance = FileStorage.get_by_id(cls, "City", id)

        if instance is None:
            print("** no instance found **")
        else:
            FileStorage.destroy(cls, "City", id)

    @classmethod
    def update(cls, id=None, args=None):
        """Update the City instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        if args is None:
            print("** arguments are missing **")
            return

        instance = FileStorage.get_by_id(cls, "City", id)

        if not instance:
            print("** no instance found **")
            return

        else:
            FileStorage.update(cls, "City", id, args)
