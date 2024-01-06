import unittest
from typing import List

def largestOddNumber(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if int(num[i])%2 == 0:
            continue
        return num[:i+1]

    return ""

class largestOddNumberTest(unittest.TestCase):
    def test_largestOddNumber_case1(self, num="52", solution="5"):
        output = largestOddNumber(num)
        self.assertEqual(output, solution)

    def test_largestOddNumber_case2(self, num="4206", solution=""):
        output = largestOddNumber(num)
        self.assertEqual(output, solution)
        
    def test_largestOddNumber_case3(self, num="35427", solution="35427"):
        output = largestOddNumber(num)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()