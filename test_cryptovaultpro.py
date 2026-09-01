# test_cryptovaultpro.py
"""
Tests for CryptoVaultPro module.
"""

import unittest
from cryptovaultpro import CryptoVaultPro

class TestCryptoVaultPro(unittest.TestCase):
    """Test cases for CryptoVaultPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoVaultPro()
        self.assertIsInstance(instance, CryptoVaultPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoVaultPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
