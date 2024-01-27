# 1207. Unique Number of Occurrences

## Intuition

The goal is to determine if the number of occurrences of each unique element in the given array is itself unique. We can achieve this by using a Counter to count the occurrences of each element and then checking if the set of these counts has the same length as the original list of counts.

## Approach

1. Use the `collections.Counter` to count the occurrences of each element in the array.
2. Extract the values (counts) from the Counter.
3. Check if the length of the set of counts is equal to the length of the original list of counts. If they are equal, it means all counts are unique.

## Complexity

- Time complexity: O(n), where n is the length of the input array. Creating the Counter and checking the lengths of sets both take linear time.
- Space complexity: O(n), as we use extra space to store the counts in the Counter.

## Code

```python
from typing import List
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr).values()
  
        return len(set(counts)) == len(counts)
```
