from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in wordSet:
                    dp[end] = True
                    break

        return dp[n]