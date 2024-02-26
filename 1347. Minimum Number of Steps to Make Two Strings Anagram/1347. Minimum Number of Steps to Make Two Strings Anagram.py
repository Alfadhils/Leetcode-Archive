from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = Counter(s)

        total = 0
        for char in freq.keys():
            diff = freq[char] - t.count(char)
            if diff > 0:
                total += diff
        return total