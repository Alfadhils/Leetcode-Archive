from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        diff = 100000
        nums.sort()
        val = 0

        for i in range(0,n):
            start, end = i + 1, n - 1

            while start < end :
                threeSum = nums[i] + nums[start] + nums[end]
                res = abs(threeSum-target)

                if res == 0:
                    return threeSum

                if res < diff:
                    diff = res
                    val = threeSum

                if threeSum < target:
                    start += 1
                else :
                    end -= 1

        return val
        
        

        

        