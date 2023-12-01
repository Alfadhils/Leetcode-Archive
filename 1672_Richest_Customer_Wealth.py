import unittest
from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    maxwealth = sum(accounts[0])
    for i in accounts:
        if sum(i)> maxwealth:
            maxwealth = sum(i)
    return maxwealth

class maximumWealthTest(unittest.TestCase):
    def test_maximumWealth_case1(self, accounts=[[1,2,3],[3,2,1]], solution=6):
        output = maximumWealth(accounts)
        self.assertEqual(output, solution)

    def test_maximumWealth_case2(self, accounts=[[1,5],[7,3],[3,5]], solution=10):
        output = maximumWealth(accounts)
        self.assertEqual(output, solution)

    def test_maximumWealth_case3(self, accounts=[[2,8,7],[7,1,3],[1,9,5]], solution=17):
        output = maximumWealth(accounts)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()