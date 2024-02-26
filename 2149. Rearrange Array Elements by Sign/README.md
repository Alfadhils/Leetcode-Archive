# 2149. Rearrange Array Elements by Sign
## Intuition
The intuition behind this problem is to rearrange the elements of the given array such that all positive elements appear at even indices and all negative elements appear at odd indices.

## Approach
To solve this problem, we can iterate through the array once and place positive elements at even indices (starting from index 0) and negative elements at odd indices (starting from index 1). We'll maintain two pointers `pos` and `neg` to keep track of the next position to place a positive and negative element, respectively.

## Complexity
- Time complexity: O(n), where n is the length of the input array `nums`.
- Space complexity: O(n), where n is the length of the input array `nums`.

## Code
```python
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        pos, neg = 0, 1
        for i in range(n):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
                
        return ans
```
