# 746. Min Cost Climbing Stairs

## Intuition
The problem can be solved using dynamic programming. We can define a recursive relation to calculate the minimum cost to reach each step.

## Approach
We create a dynamic programming array `dp` where dp[i] represents the minimum cost to reach step i. We iterate through the steps starting from 2 and calculate the minimum cost to reach each step based on the cost of the previous two steps.

## Complexity
- Time complexity: O(n)
The loop runs for each step once, so the time complexity is linear, O(n).

- Space complexity: O(n)
We use an array of size n+1 to store the minimum cost for each step, resulting in linear space complexity, O(n).

## Code
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[-1]
