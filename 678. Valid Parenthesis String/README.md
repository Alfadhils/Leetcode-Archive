# 678. Valid Parenthesis String

## Intuition
The problem involves checking whether a given string containing parentheses, represented by `(`, `)`, and `*` characters, is valid. A valid string is one where all parentheses are balanced and `*` characters can be treated as either `(` or `)`. 

## Approach
We can solve this problem by using a greedy approach. We maintain two variables, `mins` and `maxs`, representing the minimum and maximum possible count of open parentheses respectively. We iterate through the string, updating these counts based on the encountered characters:
- If we encounter `(`, both `mins` and `maxs` are incremented by 1.
- If we encounter `)`, both `mins` and `maxs` are decremented by 1.
- If we encounter `*`, we decrement `mins` by 1 (as `*` can be considered as a closing parenthesis) and increment `maxs` by 1 (as `*` can be considered as an opening parenthesis or remain unmatched).

During the iteration, if `maxs` becomes negative, it implies there are more closing parentheses encountered than opening ones, thus the string is invalid. If `mins` becomes negative, we reset it to 0, ensuring that the count of opening parentheses remains non-negative. After iterating through the entire string, we check if `mins` is zero, which indicates that all opening parentheses are matched by closing parentheses.

## Complexity
- Time complexity: O(n), where n is the length of the input string. We traverse the string once.
- Space complexity: O(1), as we use only a constant amount of extra space regardless of the input size.

## Code
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        mins, maxs = 0, 0

        for c in s:
            if c == "(":
                mins, maxs = mins + 1, maxs + 1
            elif c == ")":
                mins, maxs = mins - 1, maxs - 1
            else:
                mins, maxs = mins - 1, maxs + 1
            if maxs < 0:
                return False
            if mins < 0:
                mins = 0
        return mins == 0
```