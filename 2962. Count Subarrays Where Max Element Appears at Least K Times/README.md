# 2962. Count Subarrays Where Max Element Appears at Least K Times

## Intuition
The intuition behind this problem is to utilize a sliding window approach to count the number of subarrays where the maximum element appears at least `k` times. By maintaining a window where the maximum element satisfies the given condition, we can efficiently count the subarrays.

## Approach
The approach here utilizes a sliding window technique. We iterate through the array, maintaining a window where the maximum element occurs at least `k` times. For each element in the array, we expand the window to the right until the frequency of the maximum element within the window is less than `k`. Then, we shrink the window from the left until the frequency condition is satisfied again. At each step, we count the number of subarrays that can be formed with the current window.

## Complexity
- Time complexity:
  - The algorithm iterates through the array once, and for each element, it potentially expands and shrinks a window.
  - In the worst case, each element might cause the window to expand and shrink, resulting in a time complexity of O(n^2).
- Space complexity:
  - The algorithm uses a constant amount of extra space for variables, resulting in a space complexity of O(1).

## Code
```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxnum = max(nums)
        maxfreq = 0
        res = 0
        left = 0

        for right in range(n):
            if nums[right] == maxnum:
                maxfreq += 1
            
            while maxfreq >= k:
                if nums[left] == maxnum:
                    maxfreq -= 1
                
                left += 1
            
            res += left
                    
        return res
```