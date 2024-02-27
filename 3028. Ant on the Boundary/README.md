# 3028. Ant on the Boundary

## Intuition
The problem likely involves traversing through a list of numbers and counting occurrences when the sum of elements equals zero. This could imply that we are looking for subarrays where the cumulative sum resets to zero.

## Approach
We can iterate through the list of numbers and maintain a running sum. Whenever the sum equals zero, we increment a counter, indicating we've encountered a subarray with zero sum.

## Complexity
- Time complexity:
  - The algorithm iterates through the entire list of numbers once, resulting in a time complexity of O(n), where n is the length of the input list.
  
- Space complexity:
  - The algorithm utilizes a constant amount of extra space for variables like the counter and the sum, resulting in a space complexity of O(1).

## Code
```python
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c = 0
        sums = 0
        for n in nums:
            sums += n
            
            if sums == 0:
                c += 1
        
        return c
```