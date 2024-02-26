# 76. Minimum Window Substring
## Intuition
The problem involves finding the minimum window in string `s` that contains all the characters in string `t`. To solve this, we can use a sliding window approach.

## Approach
- Initialize two pointers `l` and `r` to track the left and right ends of the window, respectively.
- Use a dictionary to count the occurrences of characters in string `t`.
- Move the right pointer to expand the window until all characters in `t` are covered.
- Once the window covers all characters in `t`, move the left pointer to minimize the window size while still ensuring all characters in `t` are present.
- Update the minimum window size and its starting and ending indices during each iteration.

## Complexity
- Time complexity: O(m + n), where m is the length of string `s` and n is the length of string `t`. The algorithm iterates through each character in `s` once and performs constant-time operations for each character.
- Space complexity: O(n), where n is the length of string `t`. The space is primarily used for storing the character counts in `t`.

## Code 
``` python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = collections.Counter(t)
        l, r = 0, 0
        min_len = m + 1  
        res = ""

        while r < m:
            if s[r] in n:
                n[s[r]] -= 1

            while all(val <= 0 for val in n.values()):
                if r - l < min_len:
                    min_len = r - l
                    res = s[l:r+1]

                if s[l] in n:
                    n[s[l]] += 1

                l += 1

            r += 1

        return res
```
