# 1481. Least Number of Unique Integers after K Removals

## Intuition
The problem asks us to find the least number of unique integers that can be obtained after removing `k` elements from the given array. To minimize the number of unique integers, we should aim to remove the least frequent elements first.

## Approach
The approach here is to use a Counter to count the occurrences of each integer in the given array. We then iterate through the counter's elements in reversed order of their frequency (least frequent first), subtracting the frequency from k until k becomes negative. At this point, we know we've removed enough occurrences to minimize the number of unique integers. The remaining elements in the counter represent the unique integers we'll keep.

## Complexity
- Time complexity:
  The time complexity of this solution is O(n log n), where n is the number of elements in the input array. Sorting the Counter elements by frequency takes O(n log n) time, and iterating through them takes O(n) time.

- Space complexity:
  The space complexity is O(n) due to the Counter data structure, which stores the counts of each unique integer in the input array.

## Code
```python
from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        ans = 0
        for key, val in reversed(c.most_common()):
            k -= val
            if k < 0:
                ans += 1
        return ans

```