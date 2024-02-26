from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        curr = nums[0]

        for n in nums[1:]:
            if curr == n:
                count += 1
            elif count == 0:
                curr = n
            else :
                count -= 1

        return curr
        