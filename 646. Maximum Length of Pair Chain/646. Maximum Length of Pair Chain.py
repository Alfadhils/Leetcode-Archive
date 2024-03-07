from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        n = len(pairs)
        max_val, curr = 1, 1
        last = pairs[0]
        for i in range(1, n):
            if last[1] < pairs[i][0]:
                curr += 1
                max_val = max(max_val, curr)
                last = pairs[i]
        
        return max_val