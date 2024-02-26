from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def solve1d(nums,t):
            total = 0
            memo = {0: 1}
            for num in nums:
                if num - t in memo:
                    total += memo[num - t]

                memo[num] = memo.get(num, 0) + 1
            return total
            
        for row in matrix:
            for i in range(len(row)-1):
                row[i+1] += row[i]
            
        count = 0
        for i in range(len(matrix)):
            for j in range(i,-1,-1):
                if i == j:
                    cur = matrix[i][:]
                else:
                    cur = [cur[x]+matrix[j][x] for x in range(len(matrix[0]))]
                
                print(cur)
                count += solve1d(cur,target)
        
        return count
        