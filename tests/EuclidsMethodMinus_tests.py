import unittest
from GreatestCommonDenominator import EuclidsMethod


class EuclidsMethodMinusTest(unittest.TestCase):
    """This will run unit tests on Euclids Method to make sure of its correctness"""
    
    def testEuclidsMinusExample1(self):
        """checks that Eulids Method calculates the correct output (2) 
        for the given inputs (64, 46)"""
        
        output = EuclidsMethod.EuclidsMethodMinus(64, 46)
        self.assertEqual(output, 2)
        
    def testEuclidsMinusExample2(self):
        """checks that Eulids Method calculates the correct output (55) 
        when the inputs are the same (55)"""
        
        output = EuclidsMethod.EuclidsMethodMinus(55, 55)
        self.assertEqual(output, 55)
        
    def testEuclidsMinusExample3(self):
        """checks that Eulids Method calculates the correct output (11) 
        for the given inputs (55, 22)"""
        
        output = EuclidsMethod.EuclidsMethodMinus(55, 22)
        self.assertEqual(output, 11)
        
    def testEuclidsMinusExample4(self):
        """checks that Eulids Method calculates the correct output (2) 
        for the given inputs (60, 14)"""
        
        output = EuclidsMethod.EuclidsMethodMinus(60, 14)
        self.assertEqual(output, 2)
        
if __name__ == '__main__':
    unittest.main()