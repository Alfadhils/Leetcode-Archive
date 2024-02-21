# 268. Missing Number

## Intuition
The provided solution utilizes binary search to find the missing number in a sorted array of consecutive integers. 

## Approach
The approach first sorts the given array. Then, it implements a binary search algorithm to find the index where the sequence breaks, indicating the missing number.

## Complexity
- Time complexity: 
  - Sorting the array takes O(n log n) time, and binary search takes O(log n) time. Thus, the overall time complexity is O(n log n).
- Space complexity: 
  - Sorting the array in-place has a space complexity of O(1). The binary search algorithm uses only a constant amount of space, resulting in O(1) space complexity.

## Code
```python
from typing import List

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
