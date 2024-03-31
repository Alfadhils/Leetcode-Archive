# 2444. Count Subarrays With Fixed Bounds
## Intuition
The problem seems to involve counting the number of subarrays within the given bounds defined by `minK` and `maxK`. We can iterate through the array and keep track of the indices where the current element equals `minK` and `maxK`. Then, for each element, we can calculate the number of subarrays that can be formed between these indices and the current position.

## Approach
1. Iterate through the array.
2. Keep track of the indices where the current element equals `minK` and `maxK`.
3. For each element, calculate the number of subarrays between these indices and the current position.
4. Update the result accordingly.
5. Reset the start index when encountering elements outside the bounds.

## Complexity
- Time complexity:
  - The algorithm iterates through the array once, resulting in a time complexity of O(n).
- Space complexity:
  - The algorithm uses a constant amount of extra space, resulting in a space complexity of O(1).

## Code
```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res = 0
        minidx = maxidx = -1
        start = 0

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                minidx = maxidx = -1
                start = i + 1
            if nums[i] == minK:
                minidx = i
            if nums[i] == maxK:
                maxidx = i
            
            res += max(0, min(minidx, maxidx) - start + 1)

        return res
```
