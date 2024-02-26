class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n < 2:
            return 0

        matches = n//2
        return matches + self.numberOfMatches(n-matches)