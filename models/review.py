#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Return a list of all Review instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("Review."):
                result.append(str(instance))

        print(result)

    @classmethod
    def count(cls):
        """Count all Review instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("Review."):
                result.append(str(instance))

        print(len(result))

    @classmethod
    def show(cls, id):
        """Return the Review instance with the given ID"""
        result = FileStorage.get_by_id(cls, "Review", id)

        if result is None:
            print("** no instance found **")
        else:
            print(f'{result}')

    @classmethod
    def destroy(cls, id):
        """Destroy the Review instance with the given ID"""
        result = FileStorage.get_by_id(cls, "Review", id)

        if result is None:
            print("** no instance found **")
        else:
            FileStorage.destroy(cls, "Review", id)
