import unittest
from typing import List

def findPeaks(mountain: List[int]) -> List[int]:
    res = []
    for i in range(1,len(mountain)-1):
        if mountain[i]<=mountain[i-1]:
            continue
        if mountain[i]>mountain[i+1]:
            res.append(i)
    return res

class findPeaksTest(unittest.TestCase):
    def test_findPeaks_case1(self, mountain=[2,4,4], solution=[]):
        output = findPeaks(mountain)
        self.assertEqual(output, solution)

    def test_findPeaks_case2(self, mountain=[1,4,3,8,5], solution=[1,3]):
        output = findPeaks(mountain)
        self.assertEqual(output, solution)
        
    def test_findPeaks_case3(self, mountain=[3,2,4,2,2,4,4,5,4,1], solution=[2,7]):
        output = findPeaks(mountain)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()