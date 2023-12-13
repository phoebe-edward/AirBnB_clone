#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class test_review(unittest.TestCase):
    """class test_review"""

    def test_initialization(self):
        """test initialization"""
        bm6 = Review()
        self.assertEqual(bm6.place_id, "")
        self.assertEqual(bm6.user_id, "")
        self.assertEqual(bm6.text, "")
        self.assertIsInstance(bm6.place_id, str)
        self.assertIsInstance(bm6.user_id, str)
        self.assertIsInstance(bm6.text, str)
