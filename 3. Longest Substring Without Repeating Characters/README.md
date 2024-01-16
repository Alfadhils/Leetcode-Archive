# Intuition

The problem involves finding the length of the longest substring without repeating characters in a given string. My initial intuition is to use a sliding window approach, where we maintain a window of characters and update it as we traverse the string.

# Approach

The approach is to use a sliding window represented by the variables `start` and `end`. We also maintain a dictionary (`char_index`) to store the most recent index of each character encountered. If we encounter a repeating character, we update the starting index of the window (`start`) to the next index of the repeating character. We continuously update the maximum length of the substring (`max_len`) as we iterate through the string.

# Complexity

- Time complexity:

The time complexity of this solution is O(n), where n is the length of the input string. We iterate through the string once.

- Space complexity:

The space complexity is O(min(m, n)), where n is the length of the input string and m is the size of the character set. In the worst case, the character_index dictionary could store all characters in the string.

# Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
    
        char_index = {}
        max_len = 0
        start = 0 

        for end in range(n):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            char_index[s[end]] = end 
            max_len = max(max_len, end - start + 1)

        return max_len
```
