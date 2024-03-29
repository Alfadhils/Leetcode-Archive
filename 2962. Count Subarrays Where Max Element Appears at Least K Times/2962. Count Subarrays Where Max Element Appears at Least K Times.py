from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxnum = max(nums)
        maxfreq = 0
        res = 0
        left = 0

        for right in range(n):
            if nums[right] == maxnum:
                maxfreq += 1
            
            while maxfreq >= k:
                if nums[left] == maxnum:
                    maxfreq -= 1
                
                left += 1
            
            res += left
                    
        return res