# 3011. Find if Array Can Be Sorted
## Intuition
The problem asks to determine whether an array can be sorted using only one operation: swapping any two elements. One possible intuition for solving this problem is to observe that if after sorting the array, it remains the same as the original array, then it is already sorted. Otherwise, we need to check if there's only one pair of elements that are out of order and can be swapped to sort the array.

## Approach
1. Sort the array and store the sorted version.
2. Check if the sorted array is equal to the original array. If so, return `True` because the array is already sorted.
3. Iterate through the original array and find the number of 1 bits in each element.
4. Compare the number of 1 bits in consecutive elements.
5. If the number of 1 bits changes, update the maximum value encountered so far. If an element is less than the maximum value, return `False` because swapping it with a previous element won't sort the array.
6. If the number of 1 bits remains the same, compare the element with the maximum value encountered so far. If it's less than the maximum value, return `False`.
7. If all elements pass the checks, return `True`.

## Complexity
- Time complexity:  
  - Sorting the array takes (O(n log n)) time.
  - Iterating through the array and comparing elements takes (O(n)) time.
  - Overall time complexity is (O(n log n)) due to sorting.

- Space complexity:  
  - Additional space is used to store the sorted array, which takes (O(n)) space.
  - Other variables require constant space.
  - Overall space complexity is (O(n)).

## Code
```python
from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = sorted(nums)
        
        if nums == n:
            return True
        
        prev = -1
        max_val = -1
        curr_max = -1
        
        for i in range(len(nums)):
            count = bin(nums[i]).count('1')
            
            if count != prev:
                max_val = curr_max
                if nums[i] < max_val:
                    return False
                else:
                    curr_max = nums[i]
            else:
                if nums[i] < max_val:
                    return False
                else:
                    curr_max = max(curr_max, nums[i])
            
            prev = count
                
        return True
```
