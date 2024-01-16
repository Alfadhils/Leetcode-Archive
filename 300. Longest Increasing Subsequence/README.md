# 300. Longest Increasing Subsequence

## Intuition
The problem is asking to find the length of the longest increasing subsequence in an array. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. An increasing subsequence is a subsequence in which the elements are in non-decreasing order.

## Approach
The dynamic programming approach can be used to solve this problem. We can maintain an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. We initialize all elements of `dp` to 1, as the minimum length of any subsequence would be 1.

We then iterate over each element in the array, and for each element, we iterate over all previous elements to check if the current element can be included in the increasing subsequence ending at the current index. If it can, we update the length of the subsequence ending at the current index.

Finally, the maximum value in the `dp` array will be the length of the longest increasing subsequence in the given array.

## Complexity
- Time complexity: O(n^2), where n is the length of the input array `nums`. This is because we have nested loops iterating over the array.
- Space complexity: O(n), as we use an additional array `dp` of length `n` to store the length of the longest increasing subsequence ending at each index.

## Code
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```