# 1614. Maximum Nesting Depth of the Parentheses
## Intuition
The problem involves finding the maximum nesting depth of parentheses in a given string. We need to keep track of the depth while traversing the string and update the maximum depth encountered so far.

## Approach
One approach is to iterate through the string, maintaining a variable to track the current depth. Whenever an opening parenthesis is encountered, we increment the depth, and whenever a closing parenthesis is encountered, we decrement the depth. At each step, we update the maximum depth seen so far.

## Complexity
- Time complexity:
  - The time complexity of this approach is O(n), where n is the length of the input string.
- Space complexity:
  - The space complexity is O(1) since we are using constant space.

## Code
```python
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxdepth = 0
        for char in s:
            if char == '(':
                depth += 1
                maxdepth = max(maxdepth, depth)
            elif char == ')':
                depth -= 1
 
        return maxdepth
```