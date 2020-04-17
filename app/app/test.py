from django import TestCase
from app.calc import add

class CalcTests(TestCase):
    def test_add_numbers(self):
        """ test two numbers adedd together """
        self.assertEqual(add(3,8), 11)
