from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        res = 0
        prod = 1
        left = 0
        
        for right in range(n):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
        
        return res