from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums[1:])
        return sum(sorted_nums[:2]) + nums[0]