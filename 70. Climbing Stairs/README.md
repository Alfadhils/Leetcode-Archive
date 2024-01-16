# 70. Climbing Stairs

## Intuition

The problem involves finding the number of distinct ways to climb a staircase with `n` steps, where each time you can either climb 1 or 2 steps. The intuition behind the solution is to use dynamic programming to avoid redundant calculations and optimize the solution.

## Approach

The recursive function `dp` is used to calculate the number of ways to climb the stairs. It takes two parameters: `n` - the remaining number of steps to climb, and `memo` - a dictionary to store already computed results to avoid recomputation.

- Base case: If `n` is less than 3, return `n` as there is only one way to climb for 0 or 1 step, and two ways for 2 steps.
- Check if the result for the current `n` is already in the `memo`. If yes, return the stored result.
- If not, calculate the result using the recursive formula: `dp(n-1, memo) + dp(n-2, memo)`. Store the result in the `memo` for future use and return the result.

The final result is obtained by calling `dp(n, {})`, where an empty dictionary is used as the initial `memo`.

## Complexity

- Time complexity: The time complexity of the solution is O(n), where `n` is the number of steps. This is because each value is calculated only once and stored in the memo, and subsequent calls retrieve the result from the memo.
- Space complexity: The space complexity is O(n) as well, considering the space used by the memo dictionary to store results for each step.

## Code

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, memo):
            if n < 3:
                return n
        
            if n in memo:
                return memo[n]
            else:
                memo[n] = dp(n-1, memo) + dp(n-2, memo)
                return memo[n]
    
        return dp(n, {})
```
