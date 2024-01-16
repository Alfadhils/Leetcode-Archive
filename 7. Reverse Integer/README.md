
# 7. Reverse Integer

## Intuition

The problem involves reversing the digits of an integer. My initial intuition is to convert the integer to a string, reverse the string, and then convert it back to an integer. However, we need to handle the sign of the integer as well.

## Approach

The approach is to first check if the given integer is negative and store that information. Then, convert the absolute value of the integer to a string, reverse the string, and convert it back to an integer. Finally, reintroduce the sign to the reversed integer. Additionally, we need to check if the reversed integer overflows the 32-bit signed integer range.

## Complexity

- Time complexity:

The time complexity of this solution is O(log(n)), where n is the absolute value of the input integer. This is because we are converting the integer to a string, which takes O(log(n)) time.

- Space complexity:

The space complexity is O(1) as we use only a constant amount of extra space.

## Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * neg
        valid_range = -(2**31) <= res <= 2**31 - 1
        return res if valid_range else 0
```
