# 509. Fibonacci Number

## Intuition
The intuition behind solving this problem is to use dynamic programming to build a solution in a bottom-up manner. Since the Fibonacci sequence is defined as the sum of the two preceding numbers, we can use an array to store the intermediate results and build the sequence iteratively.

## Approach
The approach involves creating an array `dp` of size `n+1` to store the Fibonacci numbers up to the nth term. We initialize the base cases, where `dp[0]` is 0 and `dp[1]` is 1. Then, we iterate from the 2nd index up to the nth index, filling in the array with the sum of the two preceding Fibonacci numbers (`dp[i-1]` and `dp[i-2]`).

## Complexity
- Time complexity:
The time complexity is determined by the loop that iterates from 2 to n to fill in the `dp` array. Therefore, the time complexity is O(n).

- Space complexity:
The space complexity is determined by the size of the `dp` array, which is of size n+1. Therefore, the space complexity is O(n).

## Code
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
            
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
