# 2108. Find First Palindromic String in the Array

## Intuition
The problem asks us to find the first palindromic string in a given array of strings.

## Approach
We iterate through each string in the array and check if it is a palindrome by comparing it with its reverse. If a palindrome is found, we return it. If no palindrome is found, we return an empty string.

## Complexity
- Time complexity: O(n * m), where `n` is the number of strings in the array and `m` is the average length of the strings.
- Space complexity: O(1).

## Code
```python
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word

        return ''
```