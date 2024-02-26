# 231. Power of Two
## Intuition
The problem likely requires determining whether a given number is a power of two. To approach this, we can consider that powers of two have a specific property in binary representation.

## Approach
One common approach is to check if the number has only one '1' bit in its binary representation. If so, it is a power of two. We can achieve this by using bitwise operations or simple arithmetic.

## Complexity
- Time complexity:
The time complexity of this approach is typically O(1) since it involves simple arithmetic or bitwise operations.

- Space complexity:
The space complexity of this approach is O(1) as it doesn't require any extra space proportional to the input size.

## Code
``` python 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n ==0 :
            return False
        elif n % 2 == 0:
            return self.isPowerOfTwo(n/2)
        else :
            return False
```