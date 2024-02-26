# 150. Evaluate Reverse Polish Notation

## Intuition

The Reverse Polish Notation (RPN) is a mathematical notation in which every operator follows all of its operands. In this problem, we are given an expression in Reverse Polish Notation and asked to evaluate it.

## Approach

The approach involves using a stack to keep track of operands. We iterate through the tokens in the given list. If a token is an operand, we push it onto the stack. If it's an operator, we pop the required number of operands from the stack, perform the operation, and push the result back onto the stack. Finally, the result is the only element left in the stack.

## Complexity
- Time complexity:
  - The time complexity of the algorithm is O(n), where n is the number of tokens in the input list.
  
- Space complexity:
  - The space complexity of the algorithm is O(n), where n is the number of tokens in the input list.

## Code
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
                
        return stack[-1]
```
