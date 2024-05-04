# 2000. Reverse Prefix of Word
## Intuition
To reverse the prefix of a word up to a given character, I will iterate through the word until I encounter the target character. While iterating, I will store the characters in a string, and once I reach the target character, I will reverse this string and append the remaining characters. This approach ensures that I reverse only the prefix of the word up to the specified character.

## Approach
1. Initialize variables `start` and `end` to store the prefix and suffix of the word, respectively.
2. Iterate through the characters of the word.
3. Append each character to `end`.
4. Once the target character is found and `start` is empty, assign `start` to the current value of `end` and reset `end` to an empty string.
5. Return the reversed `start` concatenated with `end`.

## Complexity
- Time complexity:
  - The time complexity of this approach is O(n), where n is the length of the input word. This is because we iterate through each character of the word once.
- Space complexity:
  - The space complexity is also O(n) as we are storing the characters of the word in strings `start` and `end`.

## Code
```python
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        start, end = '', ''

        for x in word:
            end += x
            if x == ch and not start:
                start = end
                end = ''

        return start[::-1]+end
```