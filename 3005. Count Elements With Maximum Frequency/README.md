# 3005. Count Elements With Maximum Frequency

## Intuition
The problem asks us to count the number of elements with the maximum frequency. The unique elements with the maximum frequency can be more than one. We can solve this by using a Counter hash table to count the frequency of each element, and then count the number of elements with the highest frequency.

## Approach
We utilize a hash map `c` to count the frequency of each element. By iterating through the sorted hash map, we find the highest frequency `mcount` and add the corresponding count to `res`. We terminate the loop if the current count is no longer the highest frequency.

## Complexity Analysis
- Time complexity: 
  - The creation of the hash map takes O(n) time.
  - Sorting the hash map takes O(n log n) time.
  - Therefore, the overall time complexity is O(n log n).
- Space complexity: 
  - The hash map `c` uses O(n) space.
  - Other variables use constant space.
  - Thus, the overall space complexity is O(n).

## Code
```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        mcount = 0
        res = 0
        for val, count in c.most_common():
            mcount = max(mcount, count)
            if count != mcount:
                break
            res += count
        return res
```