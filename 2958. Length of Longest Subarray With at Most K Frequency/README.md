# 2958. Length of Longest Subarray With at Most K Frequency

## Intuition
To find the length of the longest subarray with at most k distinct elements, we can use a sliding window approach. We'll maintain a sliding window where we keep track of the frequency of each element within the window. If the number of distinct elements exceeds k, we'll shrink the window from the left side until the number of distinct elements becomes k again. Meanwhile, we'll update the maximum length of the subarray as we iterate through the array.

## Approach
- Initialize a `counter` to keep track of the frequency of elements in the current window.
- Initialize `left` pointer, `maxlen` variable to keep track of the maximum length seen so far.
- Iterate through the array using a `right` pointer, updating the `counter` and expanding the window.
- If the number of distinct elements in the window exceeds `k`, shrink the window from the `left` side until it satisfies the condition again.
- Update `maxlen` with the maximum length seen so far.
- Finally, return `maxlen`.

## Complexity
- Time complexity: O(n), where n is the length of the input array. We iterate through the array once.
- Space complexity: O(n) for the counter dictionary to store the frequency of elements.

## Code
```python
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = defaultdict(int)
        left, maxlen = 0, 0
        for right in range(n):
            counter[nums[right]] += 1
            while counter[nums[right]] > k:
                counter[nums[left]] -= 1
                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen
```