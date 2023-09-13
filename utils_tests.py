import unittest
from utils import Utils

class TestUtils(unittest.TestCase):

    def testReversedInt(self):
        self.assertEqual(Utils.Reversed(123), 321)

    def testReversedFloat(self):
        self.assertEqual(Utils.Reversed(5.67), "Invalid Input")

    def testReversedString(self):
        self.assertEqual(Utils.Reversed("abc"), "Invalid Input")

    def testFormatterInt(self):
        self.assertEqual(Utils.Formatter(89), ('0b1011001', '0o131'))

    def testFormatterFloat(self):
        self.assertEqual(Utils.Formatter(36.8), "Invalid Input")

    def testFormatterString(self):
        self.assertEqual(Utils.Formatter("xyz"), "Invalid Input")

if __name__ == "__main__":
    unittest.main()


