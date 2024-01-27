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
                    dp[j] = prev+1
                else :
                    dp[j] = max(dp[j], dp[j-1])

                prev = temp

        return max(dp)
        