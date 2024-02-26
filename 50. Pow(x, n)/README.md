# 50. Pow(x, n)
## Intuition
The problem seems to involve calculating the power of a given number efficiently. 

## Approach
The approach seems to be using recursion to divide the problem into smaller subproblems by dividing the exponent by 2 in each recursion step. Then, based on whether the exponent is even or odd, the result is calculated accordingly.

## Complexity
- Time complexity: O(log n)
  - The time complexity arises from the fact that in each recursion step, the exponent is halved, leading to a binary tree structure with a height of log n.
  
- Space complexity: O(log n)
  - The space complexity is also O(log n) due to the recursion stack.

## Code
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        
        val = self.myPow(x, n // 2)

        if n % 2 == 0:
            return val * val
        else:
            return x * val * val
```