class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitmask_count = {0: 1}
        bitmask = 0
        res = 0
        
        for char in word:
            bitmask ^= 1 << (ord(char) - ord('a'))
            
            res += bitmask_count.get(bitmask, 0)
            for i in range(10):
                alt_bitmask = bitmask ^ (1 << i)
                res += bitmask_count.get(alt_bitmask, 0)
            
            bitmask_count[bitmask] = bitmask_count.get(bitmask, 0) + 1

        return res
