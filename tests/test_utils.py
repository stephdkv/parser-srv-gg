"""
test_utils.py

Тесты для модуля utils.
"""

import unittest
from my_parser.utils import clean_text

class TestUtils(unittest.TestCase):
    
    def test_clean_text(self):
        text = "  Some text  "
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "Some text")
