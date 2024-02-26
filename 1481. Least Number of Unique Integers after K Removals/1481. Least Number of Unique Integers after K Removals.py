from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        ans = 0
        for key,val in reversed(c.most_common()):
            k -= val
            if k < 0:
                ans += 1
            
        return ans