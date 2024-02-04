#!/usr/bin/python3
"""
test for city
"""
import models
import unittest
from models.city import City
class TestEmptyStringCity(unittest.TestCase):
    """
    test for empty string
    """
    def test_empty_class_attribute(self):
        """
        test empty class attribute
        """
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

if __name__ == "__main__":
    unittest.main()

