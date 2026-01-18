# test_scrollzk.py
"""
Tests for ScrollZk module.
"""

import unittest
from scrollzk import ScrollZk

class TestScrollZk(unittest.TestCase):
    """Test cases for ScrollZk class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ScrollZk()
        self.assertIsInstance(instance, ScrollZk)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ScrollZk()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
