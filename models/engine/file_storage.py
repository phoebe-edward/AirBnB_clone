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
                                             obj.id)] = obj.to_dict()

    def save(self):
        """serializes __objects into json file with path __file_path"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            return
