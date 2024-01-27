# 1239. Maximum Length of a Concatenated String with Unique Characters

## Intuition
The problem requires finding the maximum length of a concatenated string of unique characters from a given list of strings. This means we need to explore different combinations of strings to maximize the total length while ensuring that each character appears only once in the concatenated string.

## Approach
The approach uses backtracking to explore different combinations of strings. It maintains a current length (`curr`) and a frequency dictionary (`freq`) to keep track of the characters' occurrences. The function `dp(i)` is a recursive function that explores different combinations starting from the index `i` in the list of strings.

1. If a character in the current string (`s`) is already present in the frequency dictionary, it means we cannot use this string, so we skip it.
2. Otherwise, we update the frequency dictionary and current length, recursively call the function for the next index (`j + 1`), and then revert the changes after the recursive call.

The variable `res` is used to store the maximum length found during the exploration.

## Complexity
- **Time complexity:** The time complexity of the solution depends on the number of valid combinations explored. In the worst case, it could be exponential, but the use of pruning based on character frequencies helps reduce the search space. Let's denote the total number of characters in all strings as `n`, and the number of strings as `m`. The time complexity is roughly O(2^n * m).
- **Space complexity:** The space complexity is O(n), where n is the number of unique characters across all strings. This is because the `freq` dictionary is used to keep track of character frequencies.

## Code
```python
from collections import defaultdict
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(set(s)) == len(s)]
        res, curr, freq = 0, 0, defaultdict(int)

        def dp(i):
            nonlocal res, curr

            res = max(res, curr)
            
            for j in range(i, len(arr)):
                s = arr[j]

                if any(freq[c] > 0 for c in s):
                    continue
                
                for c in s: freq[c] += 1
                curr += len(s)

                dp(j + 1)

                for c in s: freq[c] -= 1
                curr -= len(s)

        dp(0)
        return res
