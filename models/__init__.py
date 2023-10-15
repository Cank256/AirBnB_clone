#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

# Define the class mappings (models dictionary)
models = {
    'BaseModel': BaseModel,
    'User': User,
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'Review': Review,
    'State': State,
}

# Create an instance of FileStorage and pass the class mappings
storage = FileStorage(models)
storage.reload()
