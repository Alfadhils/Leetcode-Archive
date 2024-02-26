# 1480. Running Sum of 1d Array

## Intuition
The problem asks for computing the running sum of a given 1-dimensional array. The running sum of an array is obtained by adding up all the previous elements along with the current element at each index.

## Approach
To solve this problem, a simple approach is to iterate through the array and maintain a running sum. At each index, add the current element to the running sum and store it in the result array. Finally, return the result array.

## Complexity
- Time complexity: O(n), where n is the length of the input array. We traverse the array once.
- Space complexity: O(n), where n is the length of the input array. The space complexity is dominated by the result array storing the running sums.

## Code
```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            res.append(sums)
        return res
```