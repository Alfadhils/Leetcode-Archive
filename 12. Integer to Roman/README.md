
# 12. Integer to Roman

## Intuition

The problem involves converting an integer to its Roman numeral representation. One way to approach this is to use a dictionary that maps integer values to their corresponding Roman numeral symbols. The idea is to iterate through the dictionary in descending order of values and greedily subtract the largest possible value from the given number while appending the corresponding Roman numeral symbol to the result string.

## Approach

1. Create a dictionary (`int_roman_dict`) that maps integer values to their Roman numeral symbols.
2. Initialize an empty string (`res`) to store the resulting Roman numeral.
3. Iterate through the dictionary in descending order of values.
4. In each iteration, check if the current key is less than or equal to the given `num`.
   - If true, append the corresponding Roman numeral symbol to the result string, repeated as many times as the division result of `num` by the current key.
   - Subtract the product of the division result and the current key from `num`.
5. Return the final result string.

## Complexity

- Time complexity: O(13) (constant time as the dictionary has a fixed number of elements)
- Space complexity: O(1) (constant space as there are no additional data structures proportional to the input)

## Code

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        int_roman_dict = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I'
        }

        res = ''
        for key, val in int_roman_dict.items():
            while key <= num :
                res += val * (num // key)
                num -= (num // key) * key

        return res
```
