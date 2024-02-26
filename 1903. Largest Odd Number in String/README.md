# 1903. Largest Odd Number in String

## Intuition
To find the largest odd number in the given string, we can iterate through the string from right to left and check each digit. If we encounter an odd digit, we return the substring from the beginning of the string up to that digit. If there are no odd digits, we return an empty string.

## Approach
1. Iterate through the string from right to left.
2. Check if the current digit is odd.
3. If it is odd, return the substring from the beginning of the string up to the current index.
4. If no odd digit is found, return an empty string.

## Complexity
- Time complexity: O(n), where n is the length of the input string. We iterate through the string once.
- Space complexity: O(1), as we only use a constant amount of extra space for variables.

## Code
```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 0:
                continue
            return num[:i + 1]

        return ""
```
