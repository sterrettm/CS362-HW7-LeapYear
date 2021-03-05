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

    def testNotEveryHundred(self):

        # Test that years that are multiples of 100 are not
        # marked as leap years

        self.assertEqual(False, leapyear(2100))
        self.assertEqual(False, leapyear(1900))
        self.assertEqual(False, leapyear(1100))
        self.assertEqual(False, leapyear(2700))

    def testEveryFourHundred(self):

        # Test that years that are multiples of 400 are
        # marked as leap years

        self.assertEqual(True, leapyear(2000))
        self.assertEqual(True, leapyear(2400))
        self.assertEqual(True, leapyear(1600))
        self.assertEqual(True, leapyear(800))

if __name__ == "__main__":
    unittest.main()
