# 525. Contiguous Array

## Intuition
The problem requires finding the maximum length of a contiguous subarray with an equal number of 0s and 1s. One intuitive approach is to maintain a cumulative sum of the array elements where each 0 is treated as -1 and each 1 is treated as 1. Whenever the cumulative sum repeats, it indicates that the number of 0s and 1s in the subarray between these repeating cumulative sums is equal. We can then calculate the length of this subarray and update the maximum length accordingly.

## Approach
1. Initialize a cumulative sum variable (`cumsum`) to 0 and a dictionary (`count_dict`) to store cumulative sums encountered along with their corresponding indices.
2. Initialize `max_len` to 0.
3. Iterate through the array. For each element:
   - Increment the cumulative sum by adding 1 if the element is 1, or subtracting 1 if the element is 0.
   - Check if the current cumulative sum exists in the `count_dict`.
     - If it does, calculate the length of the subarray from the previous index where this cumulative sum was encountered to the current index. Update `max_len` if this length is greater than the current `max_len`.
     - If it doesn't exist, add the current cumulative sum to the `count_dict` with its index.
4. Return `max_len`.

## Complexity
- Time complexity: O(n), where n is the length of the input array `nums`. The algorithm iterates through the array once.
- Space complexity: O(n), where n is the length of the input array `nums`. The space is used to store cumulative sums and their corresponding indices in the dictionary.

## Code
```python
from typing import List
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        cumsum = 0
        count_dict = defaultdict(int)
        count_dict[0] = -1
        max_len = 0
        for i in range(n):
            cumsum += (nums[i] if nums[i]==1 else -1)
            if cumsum in count_dict:
                new_len = i - count_dict[cumsum]
                max_len = max(max_len, new_len)
            else:
                count_dict[cumsum] = i
        
        return max_len
```