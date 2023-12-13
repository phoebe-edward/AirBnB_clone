#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class test_city(unittest.TestCase):
    """class test_city"""

    def test_initialization(self):
        """test initialization"""
        bm3 = City()
        self.assertEqual(bm3.state_id, "")
        self.assertEqual(bm3.name, "")
        self.assertIsInstance(bm3.state_id, str)
        self.assertIsInstance(bm3.name, str)
