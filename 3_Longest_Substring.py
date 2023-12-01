import unittest

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n < 2:
        return n
    
    char_index = {}
    max_len = 0
    start = 0 

    for end in range(n):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        char_index[s[end]] = end 
        max_len = max(max_len, end - start + 1)

    return max_len

class lengthOfLongestSubstringTest(unittest.TestCase):
    def test_lengthOfLongestSubstring_case1(self, s="abcabcbb", solution=3):
        output = lengthOfLongestSubstring(s)
        self.assertEqual(output, solution)

    def test_lengthOfLongestSubstring_case2(self, s="bbbbb", solution=1):
        output = lengthOfLongestSubstring(s)
        self.assertEqual(output, solution)

    def test_lengthOfLongestSubstring_case3(self, s="pwwkew", solution=3):
        output = lengthOfLongestSubstring(s)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()