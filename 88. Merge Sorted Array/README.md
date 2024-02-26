# 88. Merge Sorted Array
## Intuition
The intuition behind this solution is to leverage the fact that both input arrays are already sorted. We can merge them into the first array `nums1` while ensuring that the merged array remains sorted.

## Approach
The approach is to start from the end of both arrays, `nums1 `and `nums2`, and compare elements from both arrays. We'll have three pointers: one for the end of `nums1` a, one for the end of `nums2` b, and one for the position to write in `nums1` write_index. We'll compare elements at indices a and b and place the larger element at write_index. We'll continue this process until all elements from `nums2` are merged into `nums1`, ensuring that the merged array remains sorted.

## Complexity
- Time complexity: O(m + n) where m is the length of `nums1` and n is the length of `nums2`. Since we traverse both arrays once.
- Space complexity: O(1) since we are modifying `nums1` in-place without using any extra space.

## Code
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1
```