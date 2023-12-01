import unittest
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for index, i in enumerate(nums):
        if target - i in nums[index + 1:]:
            return [index, nums[index + 1:].index(target - i) + index + 1]

class twoSumTest(unittest.TestCase):
    def test_twoSum_case1(self, nums=[2, 7, 11, 15], target=9, solution=[0,1]):
        output = twoSum(nums, target)
        self.assertEqual(output, solution)

    def test_twoSum_case2(self, nums=[3, 2, 4], target=6, solution=[1, 2]):
        output = twoSum(nums, target)
        self.assertEqual(output, solution)

    def test_twoSum_case3(self, nums=[3, 3], target=6, solution=[0,1]):
        output = twoSum(nums, target)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()
