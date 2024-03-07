# 646. Maximum Length of Pair Chain

## Intuition
The problem asks us to find the longest chain of pairs in a list of pairs. A pair is a list with two elements where `pair_1` is less than `pair_2`. A set of pairs are linked in a chain if the second value of the first pair is strictly lower than the first value of the second pair.

## Approach
To solve this, we use sorting to sort the pairs based on their first elements. We then store the current maximum value, the current pair, and the last pair. We iterate through the pairs, and if the first value is higher than the last element of the last pair, we update the max value and the last pair.

## Complexity
- Time complexity: O(n) - we only iterate through the pairs once.
- Space complexity: O(1) - we use a constant amount of space.

## Code
```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        n = len(pairs)
        max_val, curr = 1, 1
        last = pairs[0]
        for i in range(1, n):
            if last[1] < pairs[i][0]:
                curr += 1
                max_val = max(max_val, curr)
                last = pairs[i]
        
        return max_val
```