from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        cumsum = []
        for num in nums:
            res+=num
            cumsum.append(res)

        for i in range(n-1,1,-1):
            if nums[i]<cumsum[i-1]:
                return sum(nums[:i+1])

        return -1
        