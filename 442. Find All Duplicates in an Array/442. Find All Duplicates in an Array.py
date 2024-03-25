from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        prev = None
        res = []
        for n in nums:
            if n == prev:
                res.append(n)
            
            prev = n
        
        return res
        