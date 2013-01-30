import unittest
from Conversions.binary import *


class BinaryConversionsTest(unittest.TestCase):

    def setUp(self):
        self.basicInput = [
            #input, expected output
            [2, "10"]
        ]
        
        self.sizeInput = [
            #base 10, size, expected output
            [2, 5, "00010"]
        ]
        
    def testNum2Bin(self):
        
        for item in self.basicInput:
            self.assertEquals(
                num2bin(item[0]),
                item[1]
            )
    
    def testNum2BinRec(self):
        for item in self.basicInput:
            self.assertEquals(
                num2binRec(item[0]),
                item[1]
            )
    
    def testNum2BinSize(self):
        for item in self.sizeInput:
            self.assertEquals(
                num2binSize(item[0], item[1]),
                item[2]
            )
    
    def testNum2BinSizeRec(self):
        for item in self.sizeInput:
            self.assertEquals(
                num2binSizeRec(item[0], item[1]),
                item[2]
            )
    
    def testNum2binSizeRec2(self):
        for item in self.sizeInput:
            self.assertEquals(
                num2binSizeRec2(item[0], item[1]),
                item[2]
            )
