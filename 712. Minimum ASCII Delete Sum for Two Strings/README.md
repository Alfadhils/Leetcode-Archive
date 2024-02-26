# 712. Minimum ASCII Delete Sum for Two Strings

## Intuition

The problem can be approached using dynamic programming. We need to find the minimum ASCII delete sum required to make two strings equal. To do this, we can use a dynamic programming matrix to keep track of the minimum ASCII delete sum for substrings of the given strings.

## Approach

1. Initialize a dynamic programming matrix `dp` of size `(m+1) x (n+1)`, where `m` and `n` are the lengths of `s1` and `s2` respectively.
2. Iterate through the matrix and fill it using dynamic programming. 
3. Start by filling the first row and column with the cumulative ASCII values of the characters in the respective strings.
4. Then, for each cell `(i, j)` in the matrix, determine the minimum ASCII delete sum required to make the substrings `s1[:i]` and `s2[:j]` equal.
5. If the characters at positions `i-1` and `j-1` in `s1` and `s2` are equal, the current cell's value would be equal to the diagonal element (`dp[i-1][j-1]`).
6. If the characters are not equal, we have three options:
   - Delete the character at position `i-1` from `s1`, thus, the sum becomes `dp[i-1][j] + ord(s1[i-1])`.
   - Delete the character at position `j-1` from `s2`, thus, the sum becomes `dp[i][j-1] + ord(s2[j-1])`.
   - Delete both characters, thus, the sum becomes `dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1])`.
7. Finally, return the value stored in the bottom-right cell of the matrix, which represents the minimum ASCII delete sum for the entire strings.

## Complexity

- Time complexity:
  - The time complexity of this approach is O(m*n), where m and n are the lengths of the input strings `s1` and `s2` respectively. This is because we traverse through the entire dp matrix once to fill it.
- Space complexity:
  - The space complexity is also O(m*n) because we use a 2D dp matrix of size (m+1) x (n+1).

## Code

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else :
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), 
                    dp[i][j-1] + ord(s2[j-1]), 
                    dp[i-1][j-1] + ord(s1[i-1])+ ord(s2[j-1]))

        return dp[-1][-1]
```