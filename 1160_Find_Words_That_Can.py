import unittest
from typing import List

def countCharacters(words: List[str], chars: str) -> int:
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

class countCharactersTest(unittest.TestCase):
    def test_countCharacters_case1(self, words=["cat","bt","hat","tree"], chars="atach", solution=6):
        output = countCharacters(words, chars)
        self.assertEqual(output, solution)

    def test_countCharacters_case2(self, words=["hello","world","leetcode"], chars="welldonehoneyr", solution=10):
        output = countCharacters(words, chars)
        self.assertEqual(output, solution)

    def test_countCharacters_case3(self, words=["one","two","three"], chars="abcdefghijklmnopqrstuvwxyz", solution=6):
        output = countCharacters(words, chars)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()