class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def count_palindromes(left, right):
            print(left,right)
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            res += count_palindromes(i, i)
            res += count_palindromes(i, i + 1)

        return res