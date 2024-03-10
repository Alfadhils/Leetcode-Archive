# 349. Intersection of Two Arrays

## Intuition
The problem asks us to find the common elements between two arrays.

## Approach
The approach used here involves converting both input arrays into sets, which allows for efficient lookup of elements. Then, we find the intersection of these sets, which gives us the common elements. Finally, we convert the resulting set back into a list and return it.

## Complexity
- Time complexity:
  - Converting both arrays into sets takes O(n) time, where n is the size of the larger array.
  - Finding the intersection of two sets using the `&` operator takes O(min(m, n)) time, where m is the size of the smaller set.
  - Therefore, the overall time complexity is O(n + min(m, n)), which simplifies to O(n).
- Space complexity:
  - Two sets are created, each containing distinct elements from the respective arrays. Therefore, the space complexity is O(n + m), where n and m are the sizes of the input arrays. However, since we're only considering the larger set size, the space complexity simplifies to O(n).

## Code
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
```