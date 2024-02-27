from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_dict = {}
        for n in nums:
            if n in n_dict:
                n_dict[n] += 1
            else :
                n_dict[n] = 1
        
        count = 0 
        for val in n_dict.values():
            if val == 1 :
                return -1
            count += (val-1)//3 + 1
        
        return count