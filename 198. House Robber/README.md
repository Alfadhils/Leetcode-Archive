# 198. House Robber

## Intuition

The problem involves determining the maximum amount of money that can be robbed from a row of houses without robbing adjacent ones. The intuition behind the approach is to use dynamic programming to keep track of the maximum amount of money that can be robbed up to the current house. The dynamic programming array `dp` is used to store these values.

## Approach

- Initialize an array `dp` of length `n` (number of houses), where `n` is the length of the input array `nums`.
- If there are less than 3 houses, return the maximum value among them.
- Initialize the first two elements of `dp` with the values of the first two houses in the input array `nums`.
- Iterate from the third house to the last house, updating the `dp` array at each step.
  - At each step, the maximum amount that can be robbed at the current house is the maximum of the amount robbed three houses ago plus the current house's value or the amount robbed two houses ago plus the current house's value.
- Return the maximum value from the `dp` array.

## Complexity

- Time complexity: O(n), where `n` is the number of houses.
- Space complexity: O(n), as we are using an array of length `n` for dynamic programming.

## Code

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, n):
            dp[i] = max(dp[i-3], dp[i-2]) + nums[i]

        return max(dp)

```
