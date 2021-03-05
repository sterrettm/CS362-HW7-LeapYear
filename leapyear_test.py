import unittest

from leapyear import leapyear

class LeapYearTestCase(unittest.TestCase):

    def testEveryFour(self):
        # Test that every fourth year is marked as a leap year
        # Here we do not give any multiples of 100 or 400

        self.assertEqual(False, leapyear(2021))
        self.assertEqual(True,  leapyear(2020))
        self.assertEqual(True,  leapyear(1840))
        self.assertEqual(False, leapyear(1997))

if __name__ == "__main__":
    unittest.main()
