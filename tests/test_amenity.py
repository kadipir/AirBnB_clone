#!/usr/bin/python3
"""
program to test file Amenity.py
"""
import unittest
from models.amenity import Amenity
class TestEmptyClassAttributeAmenity(unittest.TestCase):
    """
    class to test for empty attribute
    """
    def test_empty_attribute_amenity(self):
        """
        test for empty attribute 
        """
        self.assertEqual((Amenity.name, "")

if __name__ == "__main__":
    unittest.main()




