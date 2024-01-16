from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        prefix = ""

        for i, char in enumerate(strs[0]):
            if all(word[i] == char for word in strs):
                prefix += char
            else:
                break

        return prefix
        