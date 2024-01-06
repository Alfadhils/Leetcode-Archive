import unittest
from typing import List

def numberOfMatches(n: int) -> int:
    if n < 2:
        return 0

    matches = n//2
    return matches + numberOfMatches(n-matches)

class numberOfMatchesTest(unittest.TestCase):
    def test_numberOfMatches_case1(self, n=7, solution=6):
        output = numberOfMatches(n)
        self.assertEqual(output, solution)

    def test_numberOfMatches_case2(self, n=14, solution=13):
        output = numberOfMatches(n)
        self.assertEqual(output, solution)
        
    def test_numberOfMatches_case3(self, n=99, solution=98):
        output = numberOfMatches(n)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()