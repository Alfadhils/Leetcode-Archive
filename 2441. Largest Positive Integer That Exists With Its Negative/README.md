# 2441. Largest Positive Integer That Exists With Its Negative
## Intuition
The problem requires finding the largest positive integer that has its negative counterpart in the given list of integers. This essentially means finding the largest absolute value that has its negative in the list.

## Approach
The approach is to sort the array first. Then, use two pointers technique to iterate from both ends towards the center of the array. We want to find pairs where the negative of the number at the left pointer equals the number at the right pointer. If we find such a pair, we return the positive number. If the negative number is greater than the positive number, we move the left pointer towards the right, else we move the right pointer towards the left. If no such pair is found, we return -1.

## Complexity
- Time complexity:
    - Sorting the array takes O(n log n) time, where n is the length of the input list.
    - The while loop runs in O(n) time as it iterates through the sorted array.
    - Overall time complexity is O(n log n) due to sorting.
- Space complexity:
    - Sorting typically requires O(n) space complexity due to the use of auxiliary space.
    - Other than that, the space complexity is O(1) as we are using constant extra space for pointers.

## Code
```python
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right and nums[left]<0 and nums[right]>0:
            if nums[left]*-1 == nums[right]:
                return nums[right]
            elif nums[left]*-1>nums[right]:
                left += 1
            elif nums[left]*-1<nums[right]:
                right -= 1

        return -1
```