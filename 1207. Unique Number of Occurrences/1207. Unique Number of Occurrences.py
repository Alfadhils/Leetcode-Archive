from typing import List 
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr).values()
        return len(set(c)) == len(c)