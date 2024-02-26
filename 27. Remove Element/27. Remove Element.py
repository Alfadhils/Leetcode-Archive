from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while i < len(nums)-j:
            if nums[i] == val:
                nums.append(nums.pop(i))
                j += 1
            else:
                i += 1
    
        return len(nums)-j