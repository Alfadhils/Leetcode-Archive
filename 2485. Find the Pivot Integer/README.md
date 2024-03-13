# 2485. Find the Pivot Integer

## Intuition
The problem seems to involve finding a pivot integer in a sequence. A pivot integer is a point where the cumulative sum of integers before it is equal to the cumulative sum of integers after it.

## Approach
To solve this problem, we can compute the cumulative sum of integers from 1 to N. Then, we iterate through the cumulative sum list and find the pivot integer where the sum of elements before it equals the sum of elements after it.

## Complexity
- Time complexity: O(n) where n is the input integer.
- Space complexity: O(n) since we store the cumulative sum list.

## Code
```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n <= 1:
            return n

        cumsum = 0
        cumsum_list = []
        for i in range(1, n + 1):
            cumsum += i
            cumsum_list.append(cumsum)
        
        prev = 0
        for i in range(1, len(cumsum_list)):
            if cumsum_list[prev] + cumsum_list[i] == cumsum_list[-1]:
                return i + 1
            
            prev = i

        return -1
```
