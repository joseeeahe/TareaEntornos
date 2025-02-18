import unittest
from github import suma, resta

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)  #  Debe dar 5
        self.assertEqual(suma(-1, 1), 0) #  Debe dar 0

    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)  #  Debe dar 3
        self.assertEqual(resta(10, 5), 5) #  Debe dar 5

if __name__ == '__main__':
    unittest.main()
