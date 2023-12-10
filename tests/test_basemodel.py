#!/usr/bin/python3
"""test using unittest"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_basemodel(unittest.TestCase):
    """class test_basemodel"""

    def test_initialization(self):
        """test initialization"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)
        self.assertRaises(TypeError, BaseModel, 89)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_str(self):
        """test __str__"""
        bm1 = BaseModel()
        self.assertEqual("[{}] ({}) {}"
                         .format(bm1.__class__.__name__, bm1.id, bm1.__dict__),
                         str(bm1))

    def test_save(self):
        """test save"""
        bm1 = BaseModel()
        d1 = bm1.updated_at
        bm1.save()
        d2 = bm1.updated_at
        self.assertNotEqual(d1, d2)

    def test_to_dict(self):
        """test to_dict"""
        bm1 = BaseModel()
        dict1 = bm1.to_dict()
        self.assertIsInstance(dict1, dict)
        self.assertEqual(dict1["id"], bm1.id)
        self.assertEqual(dict1["created_at"], bm1.created_at)
        self.assertEqual(dict1["updated_at"], bm1.updated_at)
        self.assertEqual(dict1["__class__"], bm1.__class__.__name__)
