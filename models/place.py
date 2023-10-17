#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Return a list of all Place instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("Place."):
                result.append(str(instance))

        print(result)

    @classmethod
    def count(cls):
        """Count all Place instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("Place."):
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
    def update(cls, id=None, attr=None, value=None):
        """Update the City instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        if attr is None:
            print("** attribute name missing **")
            return

        if value is None:
            print("** value missing **")
            return

        instance = FileStorage.get_by_id(cls, "City", id)

        if not instance:
            print("** no instance found **")
            return

        else:
            FileStorage.update(cls, "City", id, attr, value)
