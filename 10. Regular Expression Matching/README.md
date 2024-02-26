# 10. Regular Expression Matching

## Intuition
The problem seems like it could be solved using recursion, where we compare each character of the given string with the pattern to determine if they match.

## Approach
The approach involves using recursion with backtracking. We compare characters of the string with characters of the pattern one by one. We use a recursive function to match the string and pattern, considering cases where the pattern may contain wildcard characters like '.' or '*'. 

## Complexity
- Time complexity:
The time complexity is difficult to precisely determine due to the recursive nature of the algorithm. However, in the worst case, it could be exponential, especially when the pattern contains a lot of '*' characters.

- Space complexity:
The space complexity is also challenging to determine exactly due to the recursive calls. However, it could be at most O(n), where n is the length of the input string, considering the recursive stack space.

## Code
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
        
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:])) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
```