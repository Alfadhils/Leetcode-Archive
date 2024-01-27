from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0]*n

        for i in range(n):
            low, high = 0, i - 1
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    low = mid + 1
                else:
                    high = mid - 1

            add = dp[high] if high != -1 else 0
            dp[i] = max(dp[i-1],jobs[i][2]+add)
            
        return dp[-1]