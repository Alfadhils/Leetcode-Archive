from typing import List 
from collections import defaultdict

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(set(s)) == len(s)]
        res, curr, freq = 0, 0, defaultdict(int)

        def dp(i):
            nonlocal res, curr

            res = max(res, curr)
            
            for j in range(i, len(arr)):
                s = arr[j]

                if any(freq[c] > 0 for c in s):
                    continue
                
                for c in s: freq[c] += 1
                curr += len(s)

                dp(j + 1)

                for c in s: freq[c] -= 1
                curr -= len(s)

        dp(0)
        return res