#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class test_others(unittest.TestCase):
    """class test_others"""

    def test_initialization(self):
        """test initialization"""
        bm1 = User()
        bm2 = State()
        bm3 = City()
        bm4 = Amenity()
        bm5 = Place()
        bm6 = Review()
        self.assertEqual(bm1.email, "")
        self.assertEqual(bm1.password, "")
        self.assertEqual(bm1.first_name, "")
        self.assertEqual(bm1.last_name, "")
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm2, BaseModel)
        self.assertIsInstance(bm3, BaseModel)
        self.assertIsInstance(bm4, BaseModel)
        self.assertIsInstance(bm5, BaseModel)
        self.assertIsInstance(bm6, BaseModel)
