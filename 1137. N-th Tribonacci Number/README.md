# 1137. N-th Tribonacci Number

## Intuition
The problem is asking to find the n-th term in the Tribonacci sequence, which is similar to the Fibonacci sequence but with the sum of the three preceding terms instead of two. The intuition here is to use dynamic programming to build the sequence iteratively.

## Approach
The approach involves using a dynamic programming array `dp` to store the Tribonacci sequence values up to the desired term `n`. We start with the base cases: `dp[0] = 0`, `dp[1] = 1`, and `dp[2] = 1`. Then, we iterate from `i = 3` to `n` and calculate each term as the sum of the three preceding terms (`dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`).

## Complexity
- Time complexity: O(n) - We iterate through the range from 3 to n to compute each Tribonacci term.
- Space complexity: O(n) - We use an array of size n+1 to store the intermediate results.

## Code
```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[-1]
