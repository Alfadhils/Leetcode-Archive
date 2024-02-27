from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c = 0
        sums = 0
        for n in nums:
            sums += n
            
            if sums == 0:
                c += 1
        
        return c
        