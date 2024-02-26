# 368. Largest Divisible Subset

## Intuition

The problem asks for finding the largest divisible subset from the given list of integers. One intuitive approach is to first sort the numbers. Then, for each number, we can find the largest divisible subset ending with that number. By doing so, we can gradually build up the solution.

## Approach

1. Sort the given list of numbers.
2. Initialize two arrays: `groupSize` and `prevElement`. `groupSize[i]` represents the size of the largest divisible subset ending with the number at index `i`, and `prevElement[i]` keeps track of the previous element in that subset.
3. Iterate through each number in the sorted list. For each number, iterate through the previous numbers to check if the current number is divisible by any of them. If it is, update `groupSize[i]` accordingly.
4. Keep track of the index `maxIndex`, which represents the index with the largest divisible subset.
5. Reconstruct the largest divisible subset using the `prevElement` array starting from `maxIndex`.

## Complexity
- Time complexity: 
   - Sorting the array takes O(n log n) time.
   - The nested loops iterate over each element in the sorted array, leading to a time complexity of O(n^2).
   - Reconstructing the subset takes O(n) time.
   - Thus, the overall time complexity is O(n^2).
  
- Space complexity:
   - We use two arrays of size n (`groupSize` and `prevElement`), resulting in a space complexity of O(n).
   - Additionally, the space complexity of the returned result is also O(n).
   - Hence, the overall space complexity is O(n).

## Code
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        groupSize = [1] * n
        prevElement = [-1] * n
        maxIndex = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if groupSize[i] < 1 + groupSize[j]:
                        groupSize[i] = 1 + groupSize[j]
                        prevElement[i] = j

            if groupSize[i] > groupSize[maxIndex]:
                maxIndex = i

        result = []
        while maxIndex != -1:
            result.insert(0, nums[maxIndex])
            maxIndex = prevElement[maxIndex]

        return result
```
