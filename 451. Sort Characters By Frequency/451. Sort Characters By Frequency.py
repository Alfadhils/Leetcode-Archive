from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = ''
        for char, freq in c.most_common():
            ans += char*freq
        
        return ans
        