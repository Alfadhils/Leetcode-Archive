# 201. Bitwise AND of Numbers Range

## Intuition
The problem involves finding the bitwise AND of all numbers in a range. One intuitive approach is to start with the leftmost and rightmost numbers in the range, and keep performing bitwise AND operation until the numbers become equal.

## Approach
The provided solution iteratively performs a bitwise AND operation on the `right` number with `right - 1` until `left` becomes equal to or greater than `right`. This effectively ensures that all the bits that are different between `left` and `right` are turned off, leaving only the common bits in the result.

## Complexity
- Time complexity: O(log n) where n is the maximum of `left` and `right`, as the number of iterations depends on the number of set bits in `right`.
- Space complexity: O(1) as we are using only a constant amount of extra space.

## Code
```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return left & right
```