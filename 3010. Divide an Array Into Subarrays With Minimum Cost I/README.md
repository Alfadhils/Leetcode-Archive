# 3010. Divide an Array Into Subarrays With Minimum Cost I

## Intuition
The intuition behind this problem is to minimize the cost of dividing an array into subarrays. One approach is to sort the array and then divide it into subarrays of equal length or nearly equal lengths.

## Approach
The approach here is to sort the array `nums`, excluding the first element since we want to keep the first element at the beginning of each subarray. Then, we take the first two elements from the sorted array, which represent the smallest values after the first element in the original array. We add these two smallest values to the first element of the original array since dividing at these points would minimize the overall cost.

## Complexity
- Time complexity:
  - Sorting the array takes O(n log n) time, where n is the length of the input array `nums`. Accessing the first two elements of the sorted array and summing them takes constant time. Therefore, the overall time complexity is O(n log n).
- Space complexity:
  - Sorting the array requires additional space, but since it's not explicitly mentioned whether the space used for sorting counts towards space complexity, we'll assume it does. Therefore, the space complexity is O(n).

## Code
``` python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums[1:])
        return sum(sorted_nums[:2]) + nums[0]
        
```
