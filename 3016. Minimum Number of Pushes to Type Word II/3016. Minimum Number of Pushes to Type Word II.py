from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        c = sorted(c.items(), key=lambda x: x[1], reverse=True)
        res = 0
        for i, (key, count) in enumerate(c):
            inc = i // 8 + 1
            res += inc * count
            
        return res