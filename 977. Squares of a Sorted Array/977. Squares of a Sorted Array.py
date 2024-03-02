from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        p = n-1
        res = [0 for _ in nums]
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[p] = nums[left]**2
                left += 1
            else :
                res[p] = nums[right]**2
                right -= 1
            
            p -= 1
        
        return res
        