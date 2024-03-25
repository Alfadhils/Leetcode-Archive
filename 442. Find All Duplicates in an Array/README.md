# 442. Find All Duplicates in an Array
## Intuition
One intuitive approach is to sort the array and then iterate through it, checking for duplicates by comparing adjacent elements.

## Approach
1. Sort the array `nums`.
2. Initialize a variable `prev` to keep track of the previous element.
3. Initialize an empty list `res` to store the duplicates.
4. Iterate through the sorted array.
    - If the current element `n` is equal to the previous element `prev`, it's a duplicate. Append `n` to `res`.
    - Update `prev` to `n`.
5. Return `res`.

## Complexity
- Time complexity:
    - Sorting the array takes O(n log n) time.
    - Iterating through the sorted array takes O(n) time.
    - Overall time complexity: O(n log n)
- Space complexity:
    - Sorting the array in-place takes constant space.
    - Additional space is used to store the duplicates in `res`, which can be at most O(n).
    - Overall space complexity: O(n)

## Code
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        prev = None
        res = []
        for n in nums:
            if n == prev:
                res.append(n)
            
            prev = n
        
        return res
```