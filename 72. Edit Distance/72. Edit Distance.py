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
        