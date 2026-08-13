# test_gaszenith.py
"""
Tests for GasZenith module.
"""

import unittest
from gaszenith import GasZenith

class TestGasZenith(unittest.TestCase):
    """Test cases for GasZenith class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GasZenith()
        self.assertIsInstance(instance, GasZenith)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GasZenith()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
