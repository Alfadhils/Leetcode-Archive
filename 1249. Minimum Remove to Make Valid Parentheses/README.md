# 1249. Minimum Remove to Make Valid Parentheses

## Intuition
The problem requires removing the minimum number of parentheses from a string to make it a valid parentheses sequence. To solve this, we can iterate through the string and keep track of the indices of '(' in a stack. Whenever we encounter a ')', we check if there is a corresponding '(' in the stack. If there is, we remove it from the stack; otherwise, we mark the current ')' as excess. After processing the entire string, we combine the indices of excess ')' and unmatched '(' to remove them from the string.

## Approach
1. Initialize an empty stack to store the indices of '(' and a set to store the indices of excess ')'.
2. Iterate through the string using enumerate to keep track of the indices.
3. If the current character is '(', push its index onto the stack.
4. If the current character is ')':
    - If the stack is not empty, pop the top index from the stack (as it matches the current ')').
    - If the stack is empty, mark the current index as excess ')' and add it to the set.
5. After processing the string, combine the indices of excess ')' and unmatched '(' in the set.
6. Generate the final string by excluding characters at indices marked as excess.

## Complexity
- Time complexity: O(n), where n is the length of the input string. We traverse the string once.
- Space complexity: O(n), where n is the length of the input string. The stack and excess set can store at most n indices.

## Code
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        excess = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    excess.add(i)
        
        excess.update(stack) 
        
        return ''.join(char for i, char in enumerate(s) if i not in excess)
```            