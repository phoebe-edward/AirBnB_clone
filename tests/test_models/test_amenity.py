#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class test_amenity(unittest.TestCase):
    """class test_amenity"""

    def test_initialization(self):
        """test initialization"""
        bm4 = Amenity()
        self.assertEqual(bm4.name, "")
        self.assertIsInstance(bm4.name, str)
