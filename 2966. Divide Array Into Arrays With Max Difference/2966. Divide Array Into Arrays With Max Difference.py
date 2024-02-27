from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted((nums))
        n = len(nums)
        ans = []
        for i in range(0,n,3):
            subarray = nums[i:i+3]
            if subarray[-1] - subarray[0] > k:
                return []

            ans.append(nums[i:i+3])

        return ans
        