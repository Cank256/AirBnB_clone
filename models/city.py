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
