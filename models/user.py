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
        all_objects = FileStorage.all(User)
        return list(all_objects.values())
    
    @classmethod
    def count(cls):
        """Count all User instances"""
        all_objects = FileStorage.all(User)
        return len(all_objects)
