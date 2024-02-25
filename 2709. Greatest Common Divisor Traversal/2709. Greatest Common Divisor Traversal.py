from typing import List

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 :
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        if n == 1:
            return True
        
        nums = sorted(nums,reverse=True)
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1,n):
                if gcd(nums[i],nums[j])-1:
                    nums[j]*=nums[i]
                    break
            else:
                return False
        return True