# 15. 3Sum

## Intuition

The problem asks for finding all unique triplets in an array that sum up to zero. To solve this, we can use a two-pointer approach along with sorting the array.

## Approach

1. Sort the given array in ascending order.
2. Iterate through each element in the array.
3. For each element, use two pointers (start and end) to find a pair that sums up to the negation of the current element.
4. Handle duplicate triplets to ensure uniqueness.
5. Adjust the pointers based on the sum:
   - If the sum is zero, add the triplet to the result and move the pointers to avoid duplicates.
   - If the sum is less than zero, move the start pointer to the right.
   - If the sum is greater than zero, move the end pointer to the left.

## Complexity

- Time complexity: O(n^2)
  - The outer loop runs in O(n) time, and for each element, the two-pointer approach takes O(n) time.
- Space complexity: O(1)
  - The space used is constant, as we only use a constant amount of extra space for variables.

## Code

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i + 1, n - 1
            while start < end:
                threeSum = nums[i] + nums[start] + nums[end]
                if threeSum == 0:
                    res.append([nums[i], nums[start], nums[end]])
    
                    while (start < end) and nums[start] == nums[start + 1]:
                        start += 1
                
                    while (start < end) and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1

                elif threeSum < 0:
                    start += 1
                else:
                    end -= 1

        return res
```
