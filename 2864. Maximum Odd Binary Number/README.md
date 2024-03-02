# 2864. Maximum Odd Binary Number
## Intuition
The maximum odd binary number can be generated from the number of `1`
and `0`s by all leading `1`s followed by `0`s and `1` at the last place.
## Approach
We greedily iterate through the string to count the number of `1`s and `0`s. Then use it to generate the string result.

## Complexity
- Time complexity:
O(n) because iterating through the string once.

- Space complexity:
O(1) because all variables are constant space.

## Code
``` python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        count = -1
        for char in s:
            if char == '1':
                count += 1
        
        res = '1'*count + '0'*(n-count-1) + '1'

        return res
        
```