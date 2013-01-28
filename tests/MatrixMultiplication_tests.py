import unittest;
import numpy as np
from Matrix.MatrixMultiplication import MatrixMultiplication;


class MatrixMultiplicationTest(unittest.TestCase):

    def setUp(self):
        self.inputs = [
            {#test case 1 inputs
                'a': np.array([
                    [1,2],
                    [3,4]
                ]),
        
                'b': np.array([
                    [2,4],
                    [3,4]
                ])
            }
        ]
        
        self.results = [
            np.array([#results case 1
                [8, 12],
                [18, 28]
            ])
        ]
        
    def testMatrixMultiplication(self):
        c = MatrixMultiplication(self.inputs[0]['a'], self.inputs[0]['b'])
        
        #numpy has written their own test cases for their array data type
        np.testing.assert_array_equal(c, self.results[0])