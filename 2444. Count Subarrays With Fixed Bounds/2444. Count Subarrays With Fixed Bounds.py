from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res = 0
        minidx = maxidx = -1
        start = 0

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                minidx = maxidx = -1
                start = i + 1
            if nums[i] == minK:
                minidx = i
            if nums[i] == maxK:
                maxidx = i
            
            res += max(0, min(minidx, maxidx) - start + 1)

        return res