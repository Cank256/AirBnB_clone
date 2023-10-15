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
                    cls = self.models[class_name]  # Access class mappings via self.models
                    new_obj = cls(**value)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass
