# 907. Sum of Subarray Minimums

## Intuition
The problem involves finding the sum of minimum values of all possible subarrays of a given array. To efficiently solve this problem, we can use a monotonic stack approach. The intuition behind this approach is to maintain a stack of indices such that the elements in the stack are in increasing order. This allows us to quickly calculate the contribution of each element to the final result.

## Approach
1. Initialize an empty stack, a result variable, and an array `prev_sum` of the same length as the input array, initialized to all zeros.
2. Iterate through the given array, and for each element, pop elements from the stack while the current element is smaller than the element at the top of the stack.
3. For each popped element, calculate its contribution to the sum of minimum values using the indices in the stack.
4. Update the `prev_sum` array with the contributions calculated in step 3.
5. Push the current index onto the stack.
6. Update the result variable by adding the current element's contribution to the sum.
7. Return the final result.

## Complexity
- Time complexity: O(n)
- Space complexity: O(n)

The time complexity is O(n) because each element is pushed and popped from the stack at most once. The space complexity is O(n) because we use a stack and an additional array of the same length as the input.

## Code
```python
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        stack = []
        result = 0
        prev_sum = [0] * n

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                popped_index = stack.pop()
                prev_sum[i] += prev_sum[popped_index] + (i - popped_index) * arr[popped_index]

            stack.append(i)
            result = (result + prev_sum[i]) % mod

        return result
