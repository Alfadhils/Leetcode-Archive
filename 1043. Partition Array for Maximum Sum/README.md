# 1043. Partition Array for Maximum Sum

## Intuition

The problem involves partitioning an array into subarrays and maximizing the sum of elements after partitioning. To achieve the maximum sum, we need to consider partitioning the array in a way that maximizes the sum of each partition. Since the partition size is limited by the value of `k`, we need to find an optimal way to partition the array to maximize the overall sum. Dynamic programming seems like a suitable approach as it allows us to compute the maximum sum iteratively while considering the constraints imposed by the partition size.

## Approach

The approach utilizes dynamic programming to compute the maximum sum after partitioning the given array. It iterates through the array elements and maintains a dynamic programming array `dp`, where `dp[i]` represents the maximum sum achievable up to index `i` in the input array. Within each iteration, it calculates the maximum sum for the current partition size by considering all possible partition sizes up to `k`. It updates `dp[i]` accordingly by maximizing the sum based on the current maximum element in the partition. Finally, it returns `dp[-1]`, which represents the maximum sum achievable for the entire array.

## Complexity

- Time complexity: O(n * k), where n is the length of the input array and k is the given partition size.
  - The algorithm iterates through the array once, and for each element, it considers up to `k` previous elements to compute the maximum sum.
- Space complexity: O(n), where n is the length of the input array.
  - The space complexity is dominated by the dynamic programming array `dp`, which stores the maximum sum values for each index in the array.

## Code

```python
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            current_max = 0
            for j in range(1, min(k, i + 1) + 1):
                current_max = max(current_max, arr[i - j + 1])
                dp[i] = max(dp[i], (dp[i - j] if i - j >= 0 else 0) + current_max * j)

        return dp[-1]
```
