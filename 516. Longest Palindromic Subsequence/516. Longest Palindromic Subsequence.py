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
                        dp[j] = prev+1
                    else :
                        dp[j] = max(dp[j], dp[j-1])

                    prev = temp

            return max(dp)
        
        return LCS(s, s[::-1])