# 713. Subarray Product Less Than K
## Intuition
The problem requires finding the number of contiguous subarrays whose product is less than a given integer `k`. One intuitive approach is to use a sliding window technique. By maintaining a window and adjusting it based on the product of its elements, we can count the valid subarrays efficiently.

## Approach
- Initialize variables `res` to count the number of valid subarrays, `prod` to keep track of the product of elements within the window, and `left` to mark the start of the window.
- Iterate through the array using a sliding window defined by `left` and `right` pointers.
- Update the product by multiplying the current element with the product.
- If the product exceeds or equals `k`, move the left pointer to the right until the product is less than `k`, adjusting the window accordingly.
- Increment `res` by the number of valid subarrays for the current window.
- Return the total count of valid subarrays.

## Complexity
- Time complexity: O(n), where n is the length of the input array `nums`. The algorithm traverses the array once.
- Space complexity: O(1), as the algorithm uses only a constant amount of extra space for variables.

## Code
```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        res = 0
        prod = 1
        left = 0
        
        for right in range(n):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
        
        return res
```