from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            sword = ''.join(sorted(word))
            if sword in ans:
                ans[sword].append(word)
            else :
                ans[sword] = [word]

        return list(ans.values())
        