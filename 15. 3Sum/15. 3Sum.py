from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i + 1, n - 1
            while start < end:
                threeSum = nums[i] + nums[start] + nums[end]
                if threeSum == 0:
                    res.append([nums[i], nums[start], nums[end]])
        
                    while (start < end) and nums[start] == nums[start + 1]:
                        start += 1
                    
                    while (start < end) and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1

                elif threeSum < 0:
                    start += 1
                else:
                    end -= 1

        return res