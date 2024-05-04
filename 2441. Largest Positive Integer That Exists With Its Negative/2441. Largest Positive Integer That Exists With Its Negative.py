from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right and nums[left]<0 and nums[right]>0:
            if nums[left]*-1 == nums[right]:
                return nums[right]
            elif nums[left]*-1>nums[right]:
                left += 1
            elif nums[left]*-1<nums[right]:
                right -= 1

        return -1
        