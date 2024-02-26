from bisect import bisect_left
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        stack, dp = [], {}
        for n in nums:
            i = len(stack)
            if not stack or n > stack[-1]:
                stack.append(n)
                dp[i] = {}
            else:
                i = bisect_left(stack, n)
                stack[i] = n
            if n not in dp[i]:
                dp[i][n] = 0
            if i == 0:
                dp[i][n] += 1
            else:
                for v, c in dp[i - 1].items():
                    if n > v:
                        dp[i][n] += c
        return sum([value for value in dp[len(stack) - 1].values()])