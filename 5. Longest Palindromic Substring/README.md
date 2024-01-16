# 5. Longest Palindromic Substring

## Intuition

The problem involves finding the longest palindromic substring in a given string. My initial intuition is to use a dynamic programming approach or expand around center technique to efficiently find the solution.

## Approach

The approach is to use the "expand around center" technique. The idea is to iterate through each character in the string and treat it as a potential center of a palindrome. We then expand around the center, considering both odd and even length palindromes. The maximum length palindrome and its corresponding substring are updated as we traverse the string.

## Complexity

- Time complexity:

The time complexity of this solution is O(n^2), where n is the length of the input string. This is because, in the worst case, for each character, we may need to expand around it.

- Space complexity:

The space complexity is O(1) as no additional space is used except for variables used in the function.

## Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        start, end = 0, 0

        for i in range(n):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
```
