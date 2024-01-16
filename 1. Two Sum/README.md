# 1.Two Sum

## Intuition

The problem involves finding two numbers in an array that add up to a given target. My initial intuition is to iterate through the array and, for each element, check if the complement (target minus the current element) exists in the remaining part of the array.

## Approach

The approach is a straightforward iteration through the array. For each element, I check if the complement (target minus the current element) exists in the remaining portion of the array using a simple conditional statement. If found, I return the indices of the two elements.

## Complexity

- Time complexity:

The time complexity of this solution is O(n^2), where n is the length of the input array. This is because, in the worst case, for each element, we may need to traverse the entire remaining array to find its complement.

- Space complexity:

The space complexity is O(1) as no additional space is used except for the variables used in the function.

## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, i in enumerate(nums):
            if target - i in nums[index + 1:]:
                return [index, nums[index + 1:].index(target - i) + index + 1]
```
