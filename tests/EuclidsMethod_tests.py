import unittest
from GreatestCommonDenominator import EuclidsMethod


class EuclidsMethodTest(unittest.TestCase):
    """This will run unit tests on Euclids Method to make sure of its correctness"""
    
    def testEuclidsExample1(self):
        """checks that Eulids Method calculates the correct output (2) 
        for the given inputs (64, 46)"""
        
        output = EuclidsMethod.EuclidsMethod(64, 46)
        self.assertEqual(output, 2)
        
    def testEuclidsExample2(self):
        """checks that Eulids Method calculates the correct output (2) 
        for the given inputs (55, 22)"""
        
        output = EuclidsMethod.EuclidsMethod(55, 22)
        self.assertEqual(output, 11)
        
if __name__ == '__main__':
    unittest.main()