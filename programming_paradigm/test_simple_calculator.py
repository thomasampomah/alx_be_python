import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
   
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)


        