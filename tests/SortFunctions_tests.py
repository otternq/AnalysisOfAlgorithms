import unittest
from Sort.SortFunctions import insertionSort

class SortFunctionsTest(unittest.TestCase):

	def testInsertionSort(self):

		l = [4,6,5]
		l = insertionSort(l);

		self.assertEqual(l, [4,5,6])