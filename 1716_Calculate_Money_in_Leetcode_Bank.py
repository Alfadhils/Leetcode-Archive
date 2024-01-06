import unittest
from typing import List

def totalMoney(n: int) -> int:
        res = 0
        for i in range(n):
            res += (i%7+1)+i//7
        return res

class totalMoneyTest(unittest.TestCase):
    def test_totalMoney_case1(self, n=4, solution=10):
        output = totalMoney(n)
        self.assertEqual(output, solution)

    def test_totalMoney_case2(self, n=10, solution=37):
        output = totalMoney(n)
        self.assertEqual(output, solution)
        
    def test_totalMoney_case3(self, n=20, solution=96):
        output = totalMoney(n)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()