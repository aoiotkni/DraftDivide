# test_draftdivide.py
"""
Tests for DraftDivide module.
"""

import unittest
from draftdivide import DraftDivide

class TestDraftDivide(unittest.TestCase):
    """Test cases for DraftDivide class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftDivide()
        self.assertIsInstance(instance, DraftDivide)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftDivide()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
