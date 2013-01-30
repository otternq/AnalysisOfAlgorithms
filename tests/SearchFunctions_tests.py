import unittest
from Search.SearchFunctions import BruteForce
from Search.OtherSearchFunctions import unique, maxelem


class SearchFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.inputs = [
            [64, 46, 2],
            [55, 55, 55],
            [],
            [55, 22, 11],
            [60, 14, 2]
        ]
        
    def testBruteForce(self):
        #should find the number 2
        self.assertTrue(BruteForce(self.inputs[0], 2));
        
        #should not find the number 3
        self.assertFalse(BruteForce(self.inputs[0], 3));
        
    def testBruteForceSame(self):
        #should find the number 55
        self.assertTrue(BruteForce(self.inputs[1], 55));
        
        #should not find the number 3
        self.assertFalse(BruteForce(self.inputs[1], 3));
        
    def testBruteForceEmpty(self):
    
        #should not find the number 2
        self.assertFalse(BruteForce(self.inputs[2], 2));
        
        #should not find the number 3
        self.assertFalse(BruteForce(self.inputs[2], 3));
        
    def testUniqueTrue(self):
        #test should work because all elements in item 1 (index 0) are the different
        self.assertTrue(unique(self.inputs[0]));
        
    def testUniqueFalse(self):
        #test should fail because all elements in item 2 (index 1) are the same
        self.assertFalse(unique(self.inputs[1]));
        
    def testUniqueTrue(self):
        #test should work because item 3 (index 0) is empty
        self.assertFalse(unique(self.inputs[1]));