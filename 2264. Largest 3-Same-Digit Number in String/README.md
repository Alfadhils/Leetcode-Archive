# 2264. Largest 3-Same-Digit Number in String
## Intuition
Given a string of digits, the goal is to find the largest 3-same-digit number (i.e., a number where three adjacent digits are the same) in the string.

## Approach
The approach involves iterating through the string while maintaining a maximum value. We iterate through the string, checking each group of three adjacent digits. If we find a group where all three digits are the same, we update the maximum value with the maximum of the current maximum value and the digit found. We continue this process until we've traversed the entire string.

## Complexity
- Time complexity:
The time complexity of this solution is O(n), where n is the length of the input string num. This is because we iterate through the string once.

- Space complexity:
The space complexity is O(1). We only use a constant amount of extra space for variables like max_val and i.

## Code
```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_val = "-1"
        i = 0
        while i < len(num)-2:
            if num[i] == num[i+1] == num[i+2]:
                max_val = max(max_val, num[i])
                i += 3
            else:
                i += 1
        
        return max_val * 3 if max_val != "-1" else ""
```
