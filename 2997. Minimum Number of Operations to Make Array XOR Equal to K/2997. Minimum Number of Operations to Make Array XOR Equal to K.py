from typing import List
from functools import reduce

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = reduce(lambda x, y: x ^ y, nums)
        res = xor ^ k
        return bin(res).count('1')