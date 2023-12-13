#!/usr/bin/python3
"""class file storage"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
        obj_dict = {}
        for k in FileStorage.__objects.keys():
            obj_dict[k] = FileStorage.__objects[k].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
        except FileNotFoundError:
            return
        for v in obj_dict.values():
            cls_name = v["__class__"]
            del v["__class__"]
            self.new(eval(cls_name)(**v))
