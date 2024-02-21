class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def binary_search(arr):
            low = 0
            high = len(arr) - 1
            
            while low <= high:
                mid = (low + high) // 2
                mid_val = arr[mid]
                
                if mid_val == mid:
                    low = mid + 1
                else:
                    high = mid - 1

            return low

        nums = sorted(nums)

        return binary_search(nums)