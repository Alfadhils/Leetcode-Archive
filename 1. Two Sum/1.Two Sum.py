from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, i in enumerate(nums):
            if target - i in nums[index + 1:]:
                return [index, nums[index + 1:].index(target - i) + index + 1]