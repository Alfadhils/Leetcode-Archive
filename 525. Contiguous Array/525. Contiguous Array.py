from typing import List
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        cumsum = 0
        count_dict = defaultdict(int)
        count_dict[0] = -1
        max_len = 0
        for i in range(n):
            cumsum += (1 if nums[i]==1 else -1)
            if cumsum in count_dict:
                new_len = i - count_dict[cumsum]
                max_len = max(max_len, new_len)
            else :
                count_dict[cumsum] = i
        
        return max_len