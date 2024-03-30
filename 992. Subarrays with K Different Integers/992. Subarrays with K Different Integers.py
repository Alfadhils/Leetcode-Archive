from typing import List 
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left1, left2 = 0, 0
        count1, count2 = defaultdict(int), defaultdict(int)
        distinct1, distinct2 = 0, 0
        res = 0
        
        for right in range(n):
            if count1[nums[right]] == 0:
                distinct1 += 1
            count1[nums[right]] += 1
            
            if count2[nums[right]] == 0:
                distinct2 += 1
            count2[nums[right]] += 1
            
            while distinct1 > k:
                count1[nums[left1]] -= 1
                if count1[nums[left1]] == 0:
                    distinct1 -= 1
                left1 += 1
            
            while distinct2 > k - 1:
                count2[nums[left2]] -= 1
                if count2[nums[left2]] == 0:
                    distinct2 -= 1
                left2 += 1
                
            res += left2 - left1
        
        return res