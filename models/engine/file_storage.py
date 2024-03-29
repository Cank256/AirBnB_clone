#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self, models):
        self.models = models  # Store the class mappings

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = self.models[class_name]

                    new_obj = cls(**value)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass

    def get_by_id(self, class_name, instance_id):
        all_objects = FileStorage.all(self)
        key = f"{class_name}.{instance_id}"
        instance = all_objects.get(key, None)
        return instance

    def destroy(self, class_name, instance_id):
        all_objects = FileStorage.all(self)
        key = f"{class_name}.{instance_id}"

        if key in all_objects:
            del all_objects[key]
            FileStorage.save(self)

    def update(self, class_name, instance_id, args):
        all_objects = FileStorage.all(self)
        key = f"{class_name}.{instance_id}"
        instance = all_objects.get(key, None)

        for attr_name, attr_value in args.items():
            if hasattr(instance, attr_name):
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                setattr(instance, attr_name, attr_value)
                instance.save()
