#!/usr/bin/python3
"""class file storage"""
from models.base_model import BaseModel
import json


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets a new obj in __objects dictionary"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """serializes __objects into json file with path __file_path"""
        dict1 = {}
        for key in FileStorage.__objects.keys():
            dict1[key] = (FileStorage.__objects[key].to_dict())
        str1 = json.dumps(dict1)
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            f.write(str1)

    def reload(self):
        """deserializes file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dict1 = json.load(f)
        except FileNotFoundError:
            return
        for o in dict1.values():
            cls_name = o["__class__"]
            del o["__class__"]
            self.new(eval(cls_name)(**o))
