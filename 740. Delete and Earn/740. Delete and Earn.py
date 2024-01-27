from typing import List
import collections

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_dict = collections.Counter(nums)

        n = max(nums_dict)
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = nums_dict.get(1,0)

        for key in range(2,n+1):
            dp[key] = max(dp[key-1], dp[key-2]+key*nums_dict[key])
            
        return max(dp[-1],dp[-2])