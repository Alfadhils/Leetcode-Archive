import unittest

def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    start, end = 0, 0

    for i in range(n):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

class longestPalindromeTest(unittest.TestCase):
    def test_longestPalindrome_case1(self, s="babad", solution="aba"):
        output = longestPalindrome(s)
        self.assertEqual(output, solution)

    def test_longestPalindrome_case2(self, s="cbbd", solution="bb"):
        output = longestPalindrome(s)
        self.assertEqual(output, solution)

    def test_longestPalindrome_case3(self, s="abcdededc", solution="cdededc"):
        output = longestPalindrome(s)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()