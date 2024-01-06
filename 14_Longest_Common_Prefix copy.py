import unittest
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
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

class longestCommonPrefixTest(unittest.TestCase):
    def test_longestCommonPrefix_case1(self, strs=["flower","flow","flight"], solution="fl"):
        output = longestCommonPrefix(strs)
        self.assertEqual(output, solution)

    def test_longestCommonPrefix_case2(self, strs=["dog","racecar","car"], solution=""):
        output = longestCommonPrefix(strs)
        self.assertEqual(output, solution)

    def test_longestCommonPrefix_case3(self, strs=["caterpillar","catacombs","cataclysm"], solution="cat"):
        output = longestCommonPrefix(strs)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()