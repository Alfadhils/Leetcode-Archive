# 1235. Maximum Profit in Job Scheduling

## Intuition
The problem is a variation of the classic weighted interval scheduling problem. We are given a set of jobs, each characterized by a start time, an end time, and a profit. The goal is to maximize the total profit by selecting non-overlapping jobs.

## Approach
The approach used in the code is dynamic programming. The jobs are first sorted based on their end times. Then, for each job, we use binary search to find the index of the last non-conflicting job. We consider two cases for each job: including it in the schedule or excluding it. The dynamic programming array `dp` is used to store the maximum profit at each step.

## Complexity
- Time complexity: O(n log n) due to sorting and binary search, where n is the number of jobs.
- Space complexity: O(n) for the dynamic programming array.

## Code
```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * n

        for i in range(n):
            low, high = 0, i - 1
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    low = mid + 1
                else:
                    high = mid - 1

            add = dp[high] if high != -1 else 0
            dp[i] = max(dp[i-1], jobs[i][2] + add)
            
        return dp[-1]
