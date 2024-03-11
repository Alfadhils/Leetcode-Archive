from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a = defaultdict(int)
        for i,char in enumerate(order):
            a[char] += i
        
        def getval(c):
            return a[c]
        
        s = list(s)
        s.sort(key=getval)

        return ''.join(s)