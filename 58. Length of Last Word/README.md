# 58. Length of Last Word

## Intuition

The most straightforward approach to find the length of the last word is to iterate from the end of the string and keep track of characters until we encounter a space. This indicates the beginning of the last word. 

## Approach

1. **Add a space at the beginning:** We prepend a space character to the input string. This ensures we handle cases where the last word is at the beginning of the string or has leading spaces.
2. **Iterate from the end:** We start iterating from the second-to-last character (`len(s) - 1`) because we added a space at the beginning.
3. **Track word and count:**
   - Initialize variables `word` to 0 (to indicate no word encountered yet) and `count` to 0 (to store the length).
   - Inside the loop:
      - If the current character (`s[i]`) is not a space:
         - Set `word` to 1 to signal the start of a word.
      - If `word` is 1 (meaning we're inside a word):
         - If the current character is a space, this is the end of the word. Break the loop.
         - Otherwise, increment `count`.
4. **Return the count:** After the loop, `count` holds the length of the last word.

## Complexity

- **Time complexity:** O(n), where n is the length of the input string. In the worst case, we iterate through the entire string.
- **Space complexity:** O(1), as we only use constant extra space for variables `word` and `count`.

## Code

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = 0
        count = 0
        s = ' ' + s  # Prepend a space
        i = len(s) - 1

        while i > 0:
            if s[i] != ' ':
                word = 1

            if word:
                if s[i] == ' ':
                    break
                count += 1

            i -= 1

        return count
```