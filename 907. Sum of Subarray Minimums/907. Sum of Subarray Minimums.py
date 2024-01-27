from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        stack = []
        result = 0
        prev_sum = [0] * n

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                stack.pop()

            if not stack:
                prev_sum[i] = (i + 1) * num
            else:
                prev_sum[i] = prev_sum[stack[-1]] + (i - stack[-1]) * num

            stack.append(i)

            result = (result + prev_sum[i]) % mod

        return result
