# 977. Squares of a Sorted Array

## Intuition
The problem requires us to square all elements in a list and return its ordered list. The problem is trivial by squaring each element and sorting the resulting sequence separately. However, the problem challenges us to find an O(n) solution, which can be achieved using two pointers.

## Approach
Our approach uses two pointers to always select the highest squares possible. This is because the biggest squares in the list will always be the highest positive number or the lowest negative number, which can be extracted using the absolute function. We can then move the pointers to approach the lowest possible square.

## Complexity
- Time complexity: O(n) because the two pointers only traverse once.
- Space complexity: O(n) to store the resulting sequence.

## Code
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        p = n-1
        res = [0 for _ in nums]
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[p] = nums[left] ** 2
                left += 1
            else:
                res[p] = nums[right] ** 2
                right -= 1
            
            p -= 1
        
        return res
```