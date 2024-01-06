import unittest
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

class lengthOfLISTest(unittest.TestCase):
    def test_lengthOfLIS_case1(self, nums=[10,9,2,5,3,7,101,18], solution=4):
        output = lengthOfLIS(nums)
        self.assertEqual(output, solution)

    def test_lengthOfLIS_case2(self, nums=[0,1,0,3,2,3], solution=4):
        output = lengthOfLIS(nums)
        self.assertEqual(output, solution)

    def test_lengthOfLIS_case3(self, nums=[7,7,7,7,7,7,7], solution=1):
        output = lengthOfLIS(nums)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()