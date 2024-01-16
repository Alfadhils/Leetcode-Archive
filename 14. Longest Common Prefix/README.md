
# 14. Longest Common Prefix

## Intuition

The problem requires finding the longest common prefix among a list of strings. The intuition here is to sort the list of strings and then compare the characters at each position of the first string with the corresponding characters in the other strings.

## Approach

The provided solution takes the following approach:

1. If the input list of strings `strs` is empty, return an empty string.
2. Sort the list of strings.
3. Initialize an empty string `prefix`.
4. Iterate through the characters of the first string in the sorted list.
5. For each character, check if it matches with the corresponding character in the same position of all other strings.
6. If the character matches in all strings, append it to the `prefix`.
7. If there is a mismatch, break the loop.
8. Return the final `prefix`.

## Complexity

- Time complexity: O(n * m * log(n))
  - n is the length of the longest string in the list.
  - m is the number of strings in the list.
  - Sorting the list takes O(m * log(m)), and for each character position, there is a loop over all strings, resulting in O(n * m) comparisons.
- Space complexity: O(1)
  - The algorithm uses a constant amount of space, regardless of the input size. The space required for storing the `prefix` is proportional to the length of the common prefix, which is at most the length of the shortest string in the list.

## Code

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        prefix = ""

        for i, char in enumerate(strs[0]):
            if all(word[i] == char for word in strs):
                prefix += char
            else:
                break

        return prefix
```
