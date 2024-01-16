from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)

        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2,n):
            dp[i] = max(dp[i-3], dp[i-2])+nums[i]

        return max(dp)        