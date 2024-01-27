from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        i = 0
        c = 0
        while i < len(s) and c < len(g):
            if s[i] >= g[c]:
                c += 1
            i += 1

        return c
