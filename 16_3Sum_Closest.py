import unittest
from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    n = len(nums)
    diff = 100000
    nums.sort()
    val = 0

    for i in range(0,n):
        start, end = i + 1, n - 1

        while start < end :
            threeSum = nums[i] + nums[start] + nums[end]
            res = abs(threeSum-target)

            if res == 0:
                return threeSum

            if res < diff:
                diff = res
                val = threeSum

            if threeSum < target:
                start += 1
            else :
                end -= 1

    return val

class threeSumClosestTest(unittest.TestCase):
    def test_threeSumClosest_case1(self, nums=[-1,2,1,-4], target=1, solution=2):
        output = threeSumClosest(nums, target)
        self.assertEqual(output, solution)

    def test_threeSumClosest_case2(self, nums=[0,0,0], target=1, solution=0):
        output = threeSumClosest(nums, target)
        self.assertEqual(output, solution)

    def test_threeSumClosest_case3(self, nums=[-5,5,-4,10,-3,3], target=0, solution=1):
        output = threeSumClosest(nums, target)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()