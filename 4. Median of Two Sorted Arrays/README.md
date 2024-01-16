
# 4. Median of Two Sorted Arrays

## Intuition

The problem involves finding the median of two sorted arrays. My initial intuition is to perform a binary search on the smaller array to partition it into two halves. Then, calculate the corresponding partitions in the larger array and check if the elements in these partitions form a valid median. Adjust the partitions based on the comparison results until the correct partitions are found.

## Approach

The approach is to use binary search on the smaller array to find the correct partitions. The idea is to divide both arrays into two parts such that elements on the left side are smaller than elements on the right side. We adjust the partitions based on the comparison of the maximum and minimum elements in the partitions. The final step is to calculate the median based on the partitions.

## Complexity

- Time complexity:

The time complexity of this solution is O(log(min(m, n))), where m and n are the lengths of the input arrays. The binary search is performed on the smaller array.

- Space complexity:

The space complexity is O(1) as no additional space is used except for variables used in the function.

## Code

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        mid = n//2

        left, right = 0, n1

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = mid - partition1

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == n1 else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n2 else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if n % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return min(minRight1, minRight2)

            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        return float('nan')
```
