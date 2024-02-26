# 724. Find Pivot Index

## Intuition
The intuition behind this problem is to find a pivot index where the sum of elements to the left of the index is equal to the sum of elements to the right of the index.

## Approach
The approach taken here is to iterate through the array and at each index, calculate the sum of elements to the left and the sum of elements to the right. If these sums are equal, then return that index. Otherwise, continue iterating.

## Complexity
- Time complexity:
The time complexity of this solution is O(n), where n is the number of elements in the input array. This is because we only need to iterate through the array once.

- Space complexity:
The space complexity of this solution is O(1), because we are not using any extra space that grows with the size of the input. We are only using a constant amount of extra space for variables to store sums and indices.

## Code
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            total_sum -= nums[i]
            if left_sum == total_sum:
                return i
            left_sum += nums[i]

        return -1
```
