import unittest
from GreatestCommonDenominator import EuclidsMethod


class EuclidsMethodModTest(unittest.TestCase):
    """This will run unit tests on Euclids Method to make sure of its correctness"""
    
    def setUp(self):
        self.inputs = [
            [64, 46, 2],
            [55, 55, 55],
            [55, 22, 11],
            [60, 14, 2]
        ]
        
    def testEuclidsMod(self):
        
        for param in self.inputs:
            output = EuclidsMethod.EuclidsMethodMod(param[0], param[1])
            self.assertEqual(output, param[2])
    
    def testEuclidsModMin(self):
        
        for param in self.inputs:
            output = EuclidsMethod.EuclidsMethodModMin(param[0], param[1])
            self.assertEqual(output, param[2])
       
    def testEuclidsMinus(self):
        
        for param in self.inputs:
            output = EuclidsMethod.EuclidsMethodMinus(param[0], param[1])
            self.assertEqual(output, param[2]) 
            
    def testEuclidsBrute(self):
        
        for param in self.inputs:
            output = EuclidsMethod.EuclidsMethodBrute(param[0], param[1])
            self.assertEqual(output, param[2])     
        
if __name__ == '__main__':
    unittest.main()