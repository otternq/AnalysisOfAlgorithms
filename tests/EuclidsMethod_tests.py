import unittest
from GreatestCommonDenominator import EuclidsMethod


class EuclidsMethodTest(unittest.TestCase):
    """This will run unit tests on Euclids Method to make sure of its correctness"""
    
    def testClassExample(self):
        """checks that Eulids Method calculates the correct output (2) 
        for the given inputs (64, 46)"""
        m = 64;
        n = 46;
        
        output = EuclidsMethod.EuclidsMethod(64, 46)
        self.assertEqual(output, 2)
        
if __name__ == '__main__':
    unittest.main()