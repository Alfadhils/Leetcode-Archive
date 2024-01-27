# 740. Delete and Earn

## Intuition
The problem asks to maximize the points that can be earned by deleting elements from the given array under certain conditions. To maximize the points, we need to find a strategy that considers the value of each element and optimally selects which elements to delete.

## Approach
The approach involves dynamic programming. We create a dictionary (`nums_dict`) to count the occurrences of each unique number in the input array `nums`. Then, we iterate through the range of numbers from 1 to the maximum number in the dictionary (`n`), and for each number, we calculate the maximum points that can be earned considering whether to delete or keep that number.

The dynamic programming array `dp` is used to store the maximum points at each step. The recurrence relation is defined as follows:
`dp[key] = max(dp[key-1], dp[key-2] + key * nums_dict[key])`. Here, `dp[key]` represents the maximum points that can be earned up to the number `key`. The choice is between not deleting the current number (`dp[key-1]`) and deleting it (`dp[key-2] + key * nums_dict[key]`).

The final answer is the maximum value between the last two elements of the `dp` array.

## Complexity
- Time complexity: O(n), where `n` is the maximum number in the input array.
- Space complexity: O(n), as we use a dynamic programming array of size `n+1` to store intermediate results.

## Code
```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_dict = collections.Counter(nums)

        n = max(nums_dict)
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = nums_dict.get(1,0)

        for key in range(2,n+1):
            dp[key] = max(dp[key-1], dp[key-2]+key*nums_dict[key])
            
        return max(dp[-1],dp[-2])

