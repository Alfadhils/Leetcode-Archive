class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        i = k
        res = 1
        while i < n:
            if word[i:] == word[:n-i]:
                return res
            i += k
            res += 1
            
        return res
        