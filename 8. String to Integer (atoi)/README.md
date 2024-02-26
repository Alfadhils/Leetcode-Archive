# 8. String to Integer (atoi)

## Intuition

The problem requires converting a string representing an integer into an integer value. The key is to handle various cases such as leading whitespaces, signs, and non-digit characters.

## Approach

1. Trim leading and trailing whitespaces from the input string.
2. Handle signs (+/-) if present, and remember them.
3. Iterate through the string character by character:
   - If the character is a digit, append it to the result string.
   - If the character is not a digit, break the loop.
4. If no digits were found, set the result to 0.
5. If digits were found, convert the result string to an integer and apply the sign remembered earlier.
6. Ensure the integer result stays within the 32-bit signed integer range.

## Complexity

- Time complexity: O(n), where \(n\) is the length of the input string.
- Space complexity: O(n), the space used by the result string.

## Code

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
      
        p = ''
        if s[0] == '-':
            s = s[1:]
            p = '-'
        elif s[0] == '+':
            s = s[1:]
      
        res = ''
        for i in s:
            if i.isdigit():
                res += i
            else:
                break
      
        if not res:
            res += '0'
        else:
            res = p + res

        return min(max(int(res), -2**31), 2**31 - 1)
```
