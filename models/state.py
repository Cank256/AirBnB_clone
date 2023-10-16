#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Return a list of all State instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("State."):
                result.append(str(instance))

        print(result)

    @classmethod
    def count(cls):
        """Count all State instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("State."):
                result.append(str(instance))

        print(len(result))

    @classmethod
    def show(cls, id):
        """Return the State instance with the given ID"""
        result = FileStorage.get_by_id(cls, "State", id)

        if result is None:
            print("** no instance found **")
        else:
            print(f'{result}')

    @classmethod
    def destroy(cls, id):
        """Destroy the State instance with the given ID"""
        result = FileStorage.get_by_id(cls, "State", id)

        if result is None:
            print("** no instance found **")
        else:
            FileStorage.destroy(cls, "State", id)
