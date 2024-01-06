import unittest
from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort(), s.sort()
    i = 0
    c = 0
    while i < len(s) and c < len(g):
        if s[i] >= g[c]:
            c += 1
        i += 1

    return c

class findContentChildrenTest(unittest.TestCase):
    def test_findContentChildren_case1(self, g=[1,2,3], s=[1,1], solution=1):
        output = findContentChildren(g,s)
        self.assertEqual(output, solution)

    def test_findContentChildren_case2(self, g=[1,2], s=[1,2,3], solution=2):
        output = findContentChildren(g,s)
        self.assertEqual(output, solution)
    
    def test_findContentChildren_case3(self, g=[1,1,2,2,1,1,3,3], s=[1,2,3,4,5], solution=5):
        output = findContentChildren(g,s)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()