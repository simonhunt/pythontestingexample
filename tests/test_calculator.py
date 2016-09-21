import unittest
from calculator.Calculator import Calculator

class test_calculator(unittest.TestCase):
    def test_basic(self):
        casio = Calculator()
        answer = casio.add(2, 3)
        self.assertEqual(5, answer)
