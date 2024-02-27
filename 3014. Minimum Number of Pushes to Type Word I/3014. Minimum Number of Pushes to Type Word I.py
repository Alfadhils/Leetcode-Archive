class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        for i in range(len(word)):
            inc = i//8 + 1
            res += inc
            
        return res
        