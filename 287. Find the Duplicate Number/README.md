# 287. Find the Duplicate Number

## Intuition
The problem requires finding a duplicate number in an array. Sorting the array helps bring similar elements together, making it easier to identify duplicates.

## Approach
1. Sort the array.
2. Implement binary search to find the duplicate number.
   - Define a binary search function.
   - Check if the middle element is equal to its index.
     - If it is, check if it have the same element of the last index.
       - If it is, return the middle index.
       - if not, update the high index.
     - If not, check if the middle element is less than its index.
       - If it is, update the high index.
       - If not, update the lower index.
   - Repeat until the duplicate number is found.

## Complexity
- Time complexity: O(n log n) due to sorting.
- Space complexity: O(1)if he sorting is done in place.

## Code
```python
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
```
