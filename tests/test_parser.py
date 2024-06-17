"""
test_parser.py

Тесты для модуля parser.
"""

import unittest
from my_parser.parser import Parser

class TestParser(unittest.TestCase):
    
    def test_parse(self):
        text = "Some text to parse"
        parser = Parser(text)
        result = parser.parse()
        self.assertIsNotNone(result)
        # Другие утверждения для проверки работы парсера
