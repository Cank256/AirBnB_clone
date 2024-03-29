#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance with unique id and timestamps.

        Args:
            *args: Unused.
            **kwargs: A dictionary containing attribute names and values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                        )
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models_here = self
            FileStorage.new(self, models_here)

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        FileStorage.save(self)

    def to_dict(self):
        """
        Return a dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def all(cls):
        """Return a list of all BaseModel instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("BaseModel."):
                result.append(str(instance))

        print(result)

    @classmethod
    def count(cls):
        """Count all BaseModel instances"""
        all_objects = FileStorage.all(cls)
        result = []

        for key, instance in all_objects.items():
            if key.startswith("BaseModel."):
                result.append(str(instance))

        print(len(result))

    @classmethod
    def show(cls, id=None):
        """Return the BaseModel instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        instance = FileStorage.get_by_id(cls, "BaseModel", id)

        if instance is None:
            print("** no instance found **")
        else:
            print(f'{instance}')

    @classmethod
    def destroy(cls, id=None):
        """Destroy the BaseModel instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        instance = FileStorage.get_by_id(cls, "BaseModel", id)

        if instance is None:
            print("** no instance found **")
        else:
            FileStorage.destroy(cls, "BaseModel", id)

    @classmethod
    def update(cls, id=None, args=None):
        """Update the BaseModel instance with the given ID"""
        if id is None:
            print("** instance id missing **")
            return

        if args is None:
            print("** arguments are missing **")
            return

        instance = FileStorage.get_by_id(cls, "BaseModel", id)

        if not instance:
            print("** no instance found **")
            return

        else:
            FileStorage.update(cls, "BaseModel", id, args)
