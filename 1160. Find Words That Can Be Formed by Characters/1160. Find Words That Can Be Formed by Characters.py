from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words :
            valid = 1
            base = list(chars)
            for char in word:
                if char not in base :
                    valid = 0
                    break
                else :
                    base.remove(char)
            
            if valid :
                res+=len(word)
            
        return res