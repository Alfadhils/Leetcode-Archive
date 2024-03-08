from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        mcount = 0
        res = 0
        for val, count in c.most_common():
            mcount = max(mcount,count)
            if count != mcount:
                break

            res += count

        return res
        