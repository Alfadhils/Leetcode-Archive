# 2971. Find Polygon With the Largest Perimeter

## Intuition
The intuition behind this problem is to sort the given array of lengths in non-decreasing order, and then try to find the largest possible perimeter using the largest lengths available.

## Approach
1. Sort the input array `nums` in non-decreasing order.
2. Iterate through the sorted array and keep a cumulative sum of the lengths encountered so far.
3. Traverse the array from the end, and at each index, check if the sum of the current element and the previous two elements is greater than the sum of the remaining elements. If it is, return the sum of these three elements, as it represents the largest possible perimeter.
4. If no such perimeter is found, return -1.

## Complexity
- Time complexity: O(nlogn) due to sorting the input array.
- Space complexity: O(n) for storing the cumulative sum array.

## Code
```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        cumsum = []
        for num in nums:
            res += num
            cumsum.append(res)

        for i in range(n - 1, 1, -1):
            if nums[i] < cumsum[i - 1]:
                return sum(nums[:i + 1])

        return -1
```