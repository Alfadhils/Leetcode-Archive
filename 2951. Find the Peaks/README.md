# 2951. Find the Peaks
## Intuition
We want to find the peaks in a given list representing a mountain. A peak is defined as an element which is greater than its adjacent elements. One simple approach is to iterate through the list and check if the current element is greater than its adjacent elements. If so, we mark it as a peak.

## Approach
We iterate through the list, starting from the second element to the second-to-last element. For each element, we check if it is greater than its preceding element and also greater than its succeeding element. If both conditions are met, we consider it a peak and add its index to the result list.

## Complexity
- Time complexity:
  - This solution iterates through the list once, so the time complexity is linear in the size of the input list: O(n), where n is the number of elements in the input list.
- Space complexity:
  - The space complexity is O(1) since we're only using a constant amount of extra space for storing the result list.

## Code
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                res.append(i)
        return res
```
