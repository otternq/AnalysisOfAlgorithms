import unittest
from GreatestCommonDenominator import EuclidsMethod


class EuclidsMethodModTest(unittest.TestCase):
    """This will run unit tests on Euclids Method to make sure of its correctness"""
    
    def testEuclidsModExample1(self):
        """checks that Eulids Method calculates the correct output (2) 
        for the given inputs (64, 46)"""
        
        output = EuclidsMethod.EuclidsMethodMod(64, 46)
        self.assertEqual(output, 2)
        
    def testEuclidsModExample2(self):
        """checks that Eulids Method calculates the correct output (55) 
        when the inputs are the same (55)"""
        
        output = EuclidsMethod.EuclidsMethodMod(55, 55)
        self.assertEqual(output, 55)
        
    def testEuclidsModExample3(self):
        """checks that Eulids Method calculates the correct output (11) 
        for the given inputs (55, 22)"""
        
        output = EuclidsMethod.EuclidsMethodMod(55, 22)
        self.assertEqual(output, 11)
        
    def testEuclidsModExample4(self):
        """checks that Eulids Method calculates the correct output (2) 
        for the given inputs (60, 14)"""
        
        output = EuclidsMethod.EuclidsMethodMod(60, 14)
        self.assertEqual(output, 2)
        
if __name__ == '__main__':
    unittest.main()