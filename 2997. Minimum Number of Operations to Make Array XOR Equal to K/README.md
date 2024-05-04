# 2997. Minimum Number of Operations to Make Array XOR Equal to K
## Intuition
The intuition here is to calculate the XOR of all elements in the array and then find the number of operations required to make this XOR equal to the given value 'k'.

## Approach
1. Calculate the XOR of all elements in the array.
2. Find the XOR of the calculated XOR and the given value 'k'.
3. Count the number of set bits in the result obtained in step 2.

## Complexity
- Time complexity:
The time complexity of this approach is O(n), where n is the number of elements in the input array.
- Space complexity:
The space complexity is O(1) because we are not using any extra space that scales with the size of the input.

## Code
```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = reduce(lambda x, y: x ^ y, nums)
        res = xor ^ k
        return bin(res).count('1')
```