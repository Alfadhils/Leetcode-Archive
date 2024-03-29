from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = defaultdict(int)
        left, maxlen = 0, 0
        for right in range(n):
            counter[nums[right]] += 1
            while counter[nums[right]] > k:
                counter[nums[left]] -= 1
                left += 1

            maxlen = max(maxlen,right-left+1)

        return maxlen
        