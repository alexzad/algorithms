import unittest
import time
import numpy as np
import radixsort as algorithm
import mergesort as baseline

class Test_heapsort(unittest.TestCase):

    def test_HugeArray(self):
        A = np.random.randint(low=-1_000, high=1_000, size=1_000_000).tolist()
        B = np.copy(A).tolist()
        startA = time.time()
        A = algorithm.sort(A)
        endA = time.time()
        startB = time.time()
        B = baseline.sort(B)
        endB = time.time()
        self.assertSequenceEqual(A, B)
        d = (endA - startA) / (endB - startB)
        self.assertGreater(d, .5)
        self.assertLess(d, 5)

    def test_sortFewUnsortedElements(self):
        A = [3, 45, 1, 2, 8, 992, 9, 11, 109]
        self.assertSequenceEqual(algorithm.sort(A), [1, 2, 3, 8, 9, 11, 45, 109, 992])

    def test_sortFewSortedElements(self):
        A = [1, 5, 6, 88, 104, 999, 500, 700, 600, -456]
        self.assertSequenceEqual(algorithm.sort(A), [-456, 1, 5, 6, 88, 104, 500, 600, 700, 999])

    def test_sortWithDuplicates(self):
        A = [5, -6, 3, 1, 8, 3, 2]
        self.assertSequenceEqual(algorithm.sort(A), [-6, 1, 2, 3, 3, 5, 8])

    def test_sortSameNumber(self):
        A = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertSequenceEqual(algorithm.sort(A), [1, 1, 1, 1, 1, 1, 1, 1])

    def test_sortOneElement(self):
        A = [1]
        self.assertSequenceEqual(algorithm.sort(A), [1])

    def test_sortEmptyArray(self):
        A = []
        self.assertSequenceEqual(algorithm.sort(A), [])

if __name__ == '__main__':
    unittest.main()