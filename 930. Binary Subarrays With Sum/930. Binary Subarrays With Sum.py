from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1

        res = 0
        sums = 0
        for num in nums:
            sums += num
            if sums-goal in counter :
                res += counter[sums-goal]

            counter[sums] += 1

        return res