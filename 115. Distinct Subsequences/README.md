# 115. Distinct Subsequences

## Intuition

The problem seems like it can be solved using dynamic programming. We can try to build up the solution by considering subsequences of the given strings `s` and `t`. 

## Approach

We can use dynamic programming to solve this problem. Let's define `dp[i][j]` as the number of distinct subsequences of `s[0...i]` which equals `t[0...j]`. Then, we can fill up the `dp` array using the following logic:

- If `s[i]` and `t[j]` are equal, then `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`, since we can either consider `s[i]` to match `t[j]` or not.
- If `s[i]` and `t[j]` are not equal, then `dp[i][j] = dp[i-1][j]`, since we cannot match them.

After filling up the `dp` array, the answer will be stored in `dp[m][n]`, where `m` and `n` are the lengths of `s` and `t`, respectively.

## Complexity
- Time complexity: O(m * n), where `m` is the length of string `s` and `n` is the length of string `t`.
- Space complexity: O(m * n), for the `dp` array.

## Code
```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                
        return dp[m][n]
```