import unittest
from Hanoi.hanoi import hanoi


class HanoiMethodTest(unittest.TestCase):
    
    def testHanoi(self):
        
        hanoi(8,0,2)
