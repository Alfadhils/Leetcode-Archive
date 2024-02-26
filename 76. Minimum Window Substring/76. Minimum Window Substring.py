from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = Counter(t)
        l, r = 0, 0
        min_len = m + 1  
        res = ""

        while r < m:
            if s[r] in n:
                n[s[r]] -= 1

            while all(val <= 0 for val in n.values()):
                if r - l < min_len:
                    min_len = r - l
                    res = s[l:r+1]

                if s[l] in n:
                    n[s[l]] += 1

                l += 1

            r += 1

        return res