# 673. Number of Longest Increasing Subsequence

## Intuition
The intuition behind this solution is to utilize dynamic programming to keep track of the number of longest increasing subsequences ending at each element in the input array.

## Approach
The approach involves iterating through the input array and maintaining a stack and a dictionary (`dp`) where `dp[i]` represents the dictionary storing the count of subsequences of length `i+1`. We use binary search to find the appropriate position to insert the current element in the stack while updating the `dp` dictionary accordingly.

## Complexity
- Time complexity: The time complexity of this solution is O(n^2) due to the nested loops involved in updating the `dp` dictionary.
- Space complexity: The space complexity is also O(n^2) due to the `dp` dictionary.

## Code
```python
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
```
