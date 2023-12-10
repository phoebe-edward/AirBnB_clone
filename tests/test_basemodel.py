#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel


class test_basemodel(unittest.TestCase):
    """class test_basemodel"""

    def test_initialization(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)
        self.assertRaises(TypeError, BaseModel, 89)

    def test_str(self):
        bm1 = BaseModel()
        self.assertEqual("[{}] ({}) {}"
                         .format(bm1.__class__.__name__, bm1.id, bm1.__dict__),
                         str(bm1))
