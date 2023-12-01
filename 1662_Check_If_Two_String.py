import unittest
from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)

class arrayStringsAreEqualTest(unittest.TestCase):
    def test_arrayStringsAreEqual_case1(self, word1=["ab", "c"], word2=["a", "bc"], solution=True):
        output = arrayStringsAreEqual(word1, word2)
        self.assertEqual(output, solution)

    def test_arrayStringsAreEqual_case2(self, word1=["a", "cb"], word2=["ab", "c"], solution=False):
        output = arrayStringsAreEqual(word1, word2)
        self.assertEqual(output, solution)

    def test_arrayStringsAreEqual_case3(self, word1=["abc","abc"], word2=["abc"], solution=False):
        output = arrayStringsAreEqual(word1, word2)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()