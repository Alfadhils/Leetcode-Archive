# 516. Longest Palindromic Subsequence

## Intuition
The intuition behind this problem could be the observation that finding the longest palindromic subsequence can be approached by finding the longest common subsequence (LCS) between the string and its reverse. 

## Approach
The approach involves using dynamic programming to find the LCS between the string and its reverse. We create a 2D DP array where dp[i][j] represents the length of LCS between the first i characters of text1 and the first j characters of text2. We iterate through the characters of both strings and update the DP array accordingly.

## Complexity
- Time complexity: O(n^2) where n is the length of the input string.
- Space complexity: O(n) where n is the length of the input string.

## Code
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def LCS(text1, text2):
            n1, n2 = len(text1), len(text2)
            dp = [0]*(n1+1)
            for i in range(1, n2+1):
                prev = 0
                for j in range(1, n1+1):
                    temp = dp[j]
                    if text1[j-1] == text2[i-1]:
                        dp[j] = prev + 1
                    else:
                        dp[j] = max(dp[j], dp[j-1])
                    prev = temp
            return max(dp)
        return LCS(s, s[::-1])
```
