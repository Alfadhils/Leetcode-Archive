# 2540. Minimum Common Value

## Intuition
Given two lists of ordered sets of numbers, we are tasked to find the minimum common value of both lists. We can use sets because each number is unique, but we will use the two-pointer approach for faster computation.

## Approach
The two pointers will be the indices of both lists, `idx1` and `idx2`. While the values associated with both indexes are not the same, check which one is lower and increment accordingly. If it reaches the end, then there are no matches, and we return `-1`.

## Complexity
- Time complexity: 
  - O(n + m) at most will traverse both lists once.
- Space complexity: 
  - O(1) we only use a constant amount of space.

## Code
```python
from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1, idx2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while nums1[idx1] != nums2[idx2]:     
            if nums1[idx1] > nums2[idx2]:
                if idx2 >= n2 - 1:
                    return -1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                if idx1 >= n1 - 1:
                    return -1
                idx1 += 1
        
        return nums1[idx1]
```