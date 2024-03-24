from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        def bs(arr):
            low,high = 0, len(arr)-1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == mid:
                    if arr[mid-1] == arr[mid]:
                        return mid
                    high = mid-1
                elif arr[mid] < mid :
                    high = mid-1
                else :
                    low = mid+1
            
            return mid

        return bs(nums)