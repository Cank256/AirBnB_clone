#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# Define the class mappings (models dictionary)
models = {
    'BaseModel': BaseModel,
}

# Create an instance of FileStorage and pass the class mappings
storage = FileStorage(models)
storage.reload()
