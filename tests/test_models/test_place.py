#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class test_place(unittest.TestCase):
    """class test_place"""

    def test_initialization(self):
        """test initialization"""
        bm5 = Place()
        self.assertEqual(bm5.city_id, "")
        self.assertEqual(bm5.user_id, "")
        self.assertEqual(bm5.name, "")
        self.assertEqual(bm5.description, "")
        self.assertEqual(bm5.number_rooms, 0)
        self.assertEqual(bm5.number_bathrooms, 0)
        self.assertEqual(bm5.max_guest, 0)
        self.assertEqual(bm5.price_by_night, 0)
        self.assertEqual(bm5.latitude, 0.0)
        self.assertEqual(bm5.longitude, 0.0)
        self.assertEqual(bm5.amenity_ids, [])
        self.assertIsInstance(bm5, BaseModel)
        self.assertIsInstance(bm5.city_id, str)
        self.assertIsInstance(bm5.user_id, str)
        self.assertIsInstance(bm5.name, str)
        self.assertIsInstance(bm5.description, str)
        self.assertIsInstance(bm5.number_rooms, int)
        self.assertIsInstance(bm5.number_bathrooms, int)
        self.assertIsInstance(bm5.max_guest, int)
        self.assertIsInstance(bm5.price_by_night, int)
        self.assertIsInstance(bm5.latitude, float)
        self.assertIsInstance(bm5.longitude, float)
        self.assertIsInstance(bm5.amenity_ids, list)
