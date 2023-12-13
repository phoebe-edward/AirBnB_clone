#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class test_user(unittest.TestCase):
    """class test_user"""

    def test_initialization(self):
        """test initialization"""
        bm1 = User()
        self.assertEqual(bm1.email, "")
        self.assertEqual(bm1.password, "")
        self.assertEqual(bm1.first_name, "")
        self.assertEqual(bm1.last_name, "")
        self.assertIsInstance(bm1, BaseModel)
