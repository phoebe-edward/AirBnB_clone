#!/usr/bin/python3
"""test using unittest"""
import unittest
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class test_file_storage(unittest.TestCase):
    """class test_file_storage"""

    def test_initialization(self):
        """test initialization"""
        bm1 = BaseModel()
        models.storage.new(bm1)
        self.assertEqual(type(models.storage), FileStorage)
        self.assertIn("BaseModel." + bm1.id, models.storage.all().keys())
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm1.id, save_text)
