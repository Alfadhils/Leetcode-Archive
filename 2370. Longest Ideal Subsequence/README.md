# 2370. Longest Ideal Subsequence

## Intuition
The problem seems to involve dynamic programming, where we can iteratively update the lengths of ideal subsequences.

## Approach
The approach involves using dynamic programming to iterate over the characters of the input string and updating the lengths of ideal subsequences. We maintain a dynamic programming array `dp` where `dp[i]` represents the length of the longest ideal subsequence ending at character `i`. We iterate over the characters of the string from right to left, updating `dp` as we go.

## Complexity
- Time complexity: O(n * k) where n is the length of the input string and k is a constant representing the range of characters.
- Space complexity: O(1) since the size of the `dp` array is constant.

## Code
```python
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 27
        n = len(s)

        for i in range(n - 1, -1, -1):
            cc = s[i]
            idx = ord(cc) - ord('a')
            maxi = float('-inf')

            left = max((idx - k), 0)
            right = min((idx + k), 26)

            for j in range(left, right + 1):
                maxi = max(maxi, dp[j])

            dp[idx] = maxi + 1

        return max(dp)
```