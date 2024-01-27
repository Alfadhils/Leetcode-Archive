# 1143. Longest Common Subsequence

## Intuition
The problem asks for finding the length of the longest common subsequence (LCS) between two given strings, `text1` and `text2`. A common subsequence is a sequence of characters that appears in the same order in both strings but not necessarily consecutively. The task is to find the length of the longest such subsequence.

## Approach
The provided solution uses dynamic programming to solve the problem. It employs a 2D array `dp` to store the lengths of the LCS for different prefixes of the two strings.

1. Initialize two strings `s1` and `s2` such that `s1` is the shorter of the two input strings.
2. Initialize variables `n1` and `n2` to store the lengths of `s1` and `s2`.
3. Create a 1D array `dp` of size `(n1+1)` to store the lengths of LCS for different prefixes of `s1` and `s2`.
4. Iterate over each character in `s2` and update the `dp` array accordingly.
    - For each character in `s2`, iterate over each character in `s1`.
    - If the characters in the current positions of `s1` and `s2` are the same, update `dp[j]` to be the previous value `prev + 1`.
    - If the characters are different, update `dp[j]` to be the maximum of the previous values `dp[j]` and `dp[j-1]`.
    - Update the variable `prev` to store the previous value of `dp[j]`.
5. The final answer is the maximum value in the `dp` array, representing the length of the LCS.

## Complexity
- Time complexity: The nested loops iterate over all characters in both strings, resulting in a time complexity of O(n1 * n2), where n1 and n2 are the lengths of the input strings.
- Space complexity: The space complexity is O(n1) as it uses a 1D array of size n1+1.

## Code
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1, s2 = (text1, text2) if len(text1) < len(text2) else (text2, text1)
        n1, n2 = len(s1), len(s2)

        dp = [0]*(n1+1)

        for i in range(1, n2+1):
            prev = 0
            for j in range(1, n1+1):
                temp = dp[j]
                if s1[j-1] == s2[i-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])

                prev = temp

        return max(dp)
