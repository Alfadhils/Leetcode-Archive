# 13. Roman to Integer

## Intuition

The problem involves converting a Roman numeral string to its corresponding integer value. To do this, we need to iterate through the Roman numeral string and calculate the total integer value based on certain rules.

## Approach

We can create a dictionary (`roman_to_int`) to store the integer values corresponding to each Roman numeral. Then, we iterate through the given string and add or subtract the corresponding values based on the rules of Roman numerals. If the current numeral is smaller than the next numeral, we subtract its value; otherwise, we add its value.

## Complexity

- Time complexity: O(n), where n is the length of the input string.
- Space complexity: O(1), as the dictionary and a few variables are used, and the space is constant.

## Code

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        for i, char in enumerate(s):
            if i != len(s)-1 and roman_to_int[char] < roman_to_int[s[i+1]]:
                total += -roman_to_int[char]
            else:
                total += roman_to_int[char]
    
        return total
```
