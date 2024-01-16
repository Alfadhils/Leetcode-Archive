# 191. Number of 1 Bits

## Intuition

The problem asks to count the number of 1 bits in the binary representation of a given integer.

## Approach

The approach here is to convert the integer to its binary representation using the `bin()` function, and then count the number of '1' bits in the binary string using the `count()` method.

## Complexity

- Time complexity:

The time complexity is O(log n), where n is the input integer. This is because the `bin()` function takes O(log n) time to convert the integer to its binary representation, and the `count()` method takes O(log n) time to count the '1' bits.

- Space complexity:

The space complexity is O(log n) as well, since the binary representation of the integer is stored as a string.

## Code

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```
