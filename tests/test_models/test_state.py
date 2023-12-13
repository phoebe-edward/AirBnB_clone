#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class test_state(unittest.TestCase):
    """class test_state"""

    def test_initialization(self):
        """test initialization"""
        bm2 = State()
        self.assertEqual(bm2.name, "")
        self.assertIsInstance(bm2.name, str)
