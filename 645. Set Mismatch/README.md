# 645. Set Mismatch

## Intuition
The problem requires finding two numbers in an array, where one number is duplicated, and the other is missing. Sorting the array can simplify the process of identifying the duplicate and missing elements.

## Approach
1. Initialize two variables, `ans1` and `ans2`, to store the duplicate and missing numbers.
2. Sort the input array `nums` to make it easier to identify the duplicate and missing elements.
3. Iterate through the sorted array and compare each element with its expected value (index + 1).
   - If the current element is less than its expected value, it means it's the missing element (`ans2`).
   - If the current element is greater than its expected value, it means it's the duplicate element (`ans1`).
4. After finding either the duplicate or missing element, search for the other one within the remaining elements of the sorted array.

## Complexity
- Time complexity: O(n log n) due to the sorting step.
- Space complexity: O(n) for the sorted array.

## Code
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans1, ans2 = 0, 0
        n = len(nums)
        snums = sorted(nums)
        
        for i, val in enumerate(snums):
            if i + 1 < val:
                ans2 = i + 1
                for j, val in enumerate(snums[i:]):
                    if j + i + 2 == val:
                        ans1 = val
                break
            elif i + 1 > val:
                ans1 = val
                for j, val in enumerate(snums[i:]):
                    if j + i != val:
                        ans2 = j + i
                        break
                    ans2 = j + i + 1
                break

        return [ans1, ans2]
