# 72. Edit Distance

## Intuition
The intuition behind solving the Edit Distance problem is to identify the minimum number of operations required to transform one string into another. These operations can include insertion, deletion, or replacement of a character. By understanding the relationship between the characters of the two strings, we can devise a dynamic programming solution to find the minimum edit distance.

## Approach
This problem can be solved using dynamic programming. We create a 2D array `dp` where `dp[i][j]` represents the minimum number of operations required to convert `word1[:i]` to `word2[:j]`. We iterate through both words and fill the array according to the following conditions:
- If the characters at the current positions are the same, we simply take the value from the diagonal, `dp[i-1][j-1]`.
- If the characters are different, we take the minimum of three operations:
  - Insertion: `dp[i][j-1] + 1`
  - Deletion: `dp[i-1][j] + 1`
  - Replacement: `dp[i-1][j-1] + 1`
  
Finally, we return `dp[m][n]`, where `m` and `n` are the lengths of `word1` and `word2` respectively.

## Complexity
- Time complexity: O(m * n), where m is the length of word1 and n is the length of word2.
- Space complexity: O(m * n), for the dynamic programming table `dp`.

## Code
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if (not n) or (not m):
            return abs(n-m)

        dp = [[0]*(n+1) for _ in range((m+1))]

        dp[0][0] = 1 if word1[0]!=word2[0] else 0

        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else :
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                
        return dp[-1][-1]
```