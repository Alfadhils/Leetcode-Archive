# 930. Binary Subarrays With Sum

## Intuition
The problem revolves around counting the number of subarrays within a binary array that sum up to a given target value. One intuitive approach could be to iterate through the array and for each starting index, keep track of the sum of subarrays starting from that index. Then, count the occurrences of the target sum within those subarrays.

## Approach
To efficiently solve this problem, we can utilize a hash map to store the count of sums encountered so far. We maintain a running sum while iterating through the array, and at each step, we check if there exists a subarray ending at the current position whose sum equals the target. If such a subarray exists, we increment our result count by the corresponding count stored in the hash map. Additionally, we update the hash map with the count of the current sum.

## Complexity
- Time complexity: O(n), where n is the length of the input array. We iterate through the array once.
- Space complexity: O(n), where n is the length of the input array. We use a hash map to store counts.

## Code
```python
from collections import defaultdict
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1

        res = 0
        sums = 0
        for num in nums:
            sums += num
            if sums - goal in counter:
                res += counter[sums - goal]

            counter[sums] += 1

        return res
```