from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        curr = 1
        for n in nums:
            if n>0:
                if n == curr:
                    curr+=1
                else :
                    break
        
        return curr
        