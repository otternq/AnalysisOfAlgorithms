import unittest

from GreatestCommonDenominator import EuclidsMethod


class EuclidsMethodTest(unittest.TestCase):

    def testClassExample(self):
        m = 64;
        n = 46;
        
        o = EuclidsMethod.EuclidsMethod(64, 46)
        self.assertEqual(o, 2)
        

if __name__ == '__main__':
    unittest.main()