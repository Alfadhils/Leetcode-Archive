# 1544. Make The String Great
## Intuition
We aim to eliminate pairs of adjacent characters in the string if they are of the same character but different cases (e.g., `a` and `A`, `b` and `B`).

## Approach
We use a stack to keep track of characters while iterating through the string. If the current character and the top character of the stack form a pair, we pop the stack. Otherwise, we add the current character to the stack.

## Complexity
- Time complexity: O(n), where n is the length of the string.
- Space complexity: O(n), where n is the length of the string.

## Code
```python
class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if stack:
                prev = stack[-1]
                if s[i] != prev and (s[i] == prev.upper() or s[i] == prev.lower()):
                    stack.pop()
                    continue
            stack.append(s[i])

        return ''.join(stack)
```
