import unittest
from typing import List

def runningSum(nums: List[int]) -> List[int]:
    res = []
    sums = 0
    for i in range(len(nums)):
        sums += nums[i]
        res.append(sums)
    return res

class runningSumTest(unittest.TestCase):
    def test_runningSum_case1(self, nums=[1,2,3,4], solution=[1,3,6,10]):
        output = runningSum(nums)
        self.assertEqual(output, solution)

    def test_runningSum_case2(self, nums=[1,1,1,1,1], solution=[1,2,3,4,5]):
        output = runningSum(nums)
        self.assertEqual(output, solution)

    def test_runningSum_case3(self, nums=[3,1,2,10,1], solution=[3,4,6,16,17]):
        output = runningSum(nums)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()