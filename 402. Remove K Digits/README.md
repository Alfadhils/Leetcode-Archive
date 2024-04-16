# 402. Remove K Digits
## Intuition
The problem seems to involve removing digits from a number to create the smallest possible number. We can utilize a stack to keep track of the digits while maintaining the property of forming the smallest number.

## Approach
We iterate through each digit of the number, comparing it with the digits in the stack. If the digit is smaller than the top of the stack, we remove elements from the stack until the condition is met or until we have removed k digits. After the iteration, if there are still remaining digits to be removed, we simply remove them from the end of the stack. Finally, we construct the result string from the elements in the stack.

## Complexity
- Time complexity: O(n), where n is the length of the input number.
- Space complexity: O(n), where n is the length of the input number.

## Code
```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ""
            
        stack = []
        stack.append(num[0])
        
        for i in range(1, len(num)):
            digit = num[i]
            
            while stack and stack[-1] > digit and k:
                stack.pop()
                k -= 1
            
            stack.append(digit)
        
        while k:
            stack.pop()
            k -= 1
        
        res = "".join(stack).lstrip("0")
        
        return res if res != "" else "0"
```