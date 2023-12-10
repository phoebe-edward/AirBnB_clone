#!/usr/bin/python3
"""base model"""
from uuid import uuid4
import cmd
from datetime import datetime


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialize a BaseModel"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if (kwargs and len(kwargs) != 0):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    self.created_at = datetime.strptime(v, tform)
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v, tform)
                elif k == "__class__":
                    pass
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """return string"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """convert to dictionary"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
