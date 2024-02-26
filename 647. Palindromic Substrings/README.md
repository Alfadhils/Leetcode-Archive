# 647. Palindromic Substrings

## Intuition

The intuition here is to expand around each character in the string and count the palindromic substrings by checking if the characters on both sides are equal.

## Approach

We iterate through each character in the string and consider it as a center of a potential palindrome. We then expand around this center to both sides, checking if the characters are equal. We do this for both odd-length and even-length palindromes.

## Complexity

- Time complexity:

  - The time complexity of this approach is O(n^2), where n is the length of the input string. This is because for each character, we may potentially expand up to the entire length of the string.
- Space complexity:

  - The space complexity of this approach is O(1), as we are not using any extra space that grows with the input size.

## Code

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def count_palindromes(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            res += count_palindromes(i, i)
            res += count_palindromes(i, i + 1)

        return res
```
