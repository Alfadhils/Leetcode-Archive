from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def total_product(nums):
            product = 1
            for num in nums:
                product *= num
            return product

        n = len(nums)
        res = [0]*n
        product = total_product(nums)
        for i in range(n):
            if nums[i] == 0 :
                left = total_product(nums[0:i]) if nums[0:i] else 1
                right = total_product(nums[i+1:n+1]) if nums[i+1:n+1] else 1
                res[i] = left*right
            else :
                res[i] = product//nums[i]
        
        return res
        