# 629. K Inverse Pairs Array

## Intuition
The problem seems to involve dynamic programming to calculate the number of arrays with k inverse pairs. We can use a bottom-up approach to build the solution iteratively.

## Approach
I'll break down the provided code:

1. Initialize `mod` as 10^9 + 7, which is commonly used for modulo operations.
2. Create an array `dp` of size k+1 and initialize it with zeros. This array will be used to store intermediate results for dynamic programming.
3. Set `dp[0]` to 1, as there is one way to have 0 inverse pairs (an array with elements in ascending order).
4. Iterate over the range from 1 to n (exclusive).
    - Inside this loop, initialize `count` to 0 and create an empty list `temp` to store updated dynamic programming results.
    - Iterate over the range from 0 to k (inclusive).
        - Increment `count` by the value at `dp[j]`.
        - If `j` is greater than `i`, decrement `count` by the value at `dp[j-i-1]`. This step ensures that we consider only valid inverse pairs.
        - Update `count` with the modulo operation `count % mod`.
        - Append the updated `count` to the `temp` list.
    - Update `dp` with the values from the `temp` list.
5. Return the final result stored in `dp[k]`.

## Complexity
- Time complexity: O(n * k)
- Space complexity: O(k)

## Code
```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        dp = [0]*(k+1)
        dp[0] = 1

        for i in range(1, n):
            count = 0
            temp = []
            for j in range(k+1):
                count += dp[j]
                if j > i:
                    count -= dp[j-i-1]
                
                count %= mod
                temp.append(count)
            
            dp = temp
        
        return dp[k]
