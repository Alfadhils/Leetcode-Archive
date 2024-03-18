from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def bs(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] == target[0]:
                    return mid
                elif arr[mid][0] < target[0]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        insertIdx = bs(intervals, newInterval)
        intervals.insert(insertIdx, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

        