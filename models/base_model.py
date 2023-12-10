#!/usr/bin/python3
"""base model"""
import uuid
import cmd
from datetime import datetime


class BaseModel:
    """class BaseModel"""

    def __init__(self):
        """initialize a BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
    def __str__(self):
        """return string"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """convert to dictionary"""
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
