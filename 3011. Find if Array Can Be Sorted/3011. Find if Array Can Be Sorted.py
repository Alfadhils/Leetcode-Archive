from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = sorted(nums)
        if nums == n:
            return True
        
        prev = -1
        max_val = -1
        curr_max = -1
        for i in range(len(nums)):
            count = bin(nums[i]).count('1')
            if count != prev:
                max_val = curr_max
                if nums[i]<max_val:
                    return False
                else :
                    curr_max = nums[i]

            else :
                if nums[i]<max_val:
                    return False
                else :
                    curr_max = max(curr_max, nums[i])
            
            prev = count
                
        return True
        