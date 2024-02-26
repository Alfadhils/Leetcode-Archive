from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            res.append(sums)
        return res