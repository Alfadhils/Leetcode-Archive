# 1074. Number of Submatrices That Sum to Target
## Intuition
The problem can be solved using the prefix sum technique along with the concept of hashing to efficiently count the number of submatrices that sum to the target.

## Approach
1. Define a helper function `solve1d(nums, t)` to count the number of subarrays in a 1D array `nums` that sum to the target `t`.
2. Transform the input matrix into a prefix sum matrix along the rows.
3. Iterate through all pairs of rows (i, j) where i <= j.
4. For each pair of rows, construct the cumulative sum array `cur`, which represents the sum of elements from row i to row j for each column.
5. Apply the `solve1d` function on the `cur` array to count the number of subarrays that sum to the target.
6. Accumulate the counts obtained from each `solve1d` call to get the total count of submatrices that sum to the target.

## Complexity
- Time complexity: 
  - Building the prefix sum matrix takes O(m * n^2) time, where m is the number of rows and n is the number of columns in the matrix.
  - For each pair of rows, constructing the cumulative sum array takes O(n) time, and calling `solve1d` function takes O(n) time. Hence, the total time complexity is O(m * n^2).
- Space complexity:
  - The space complexity is O(n) for the `memo` dictionary used in the `solve1d` function.
  - Additional space is used for the prefix sum matrix, which is O(m * n), where m is the number of rows and n is the number of columns in the matrix.
  - Overall, the space complexity is O(m * n) for the prefix sum matrix and O(n) for the `memo` dictionary.

## Code
```python
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def solve1d(nums, t):
            total = 0
            memo = {0: 1}
            for num in nums:
                if num - t in memo:
                    total += memo[num - t]
                memo[num] = memo.get(num, 0) + 1
            return total
            
        for row in matrix:
            for i in range(len(row) - 1):
                row[i + 1] += row[i]
            
        count = 0
        for i in range(len(matrix)):
            for j in range(i, -1, -1):
                if i == j:
                    cur = matrix[i][:]
                else:
                    cur = [cur[x] + matrix[j][x] for x in range(len(matrix[0]))]
                count += solve1d(cur, target)
        
        return count
```