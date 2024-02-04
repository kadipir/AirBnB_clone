#!/usr/bin/python3
"""
test for city
"""
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
        self.assertEqual(State.state_id, "")
        self.assertEqual(State.name, "")

if __name__ == "__main__":
    unittest.main()

