import unittest
from typing import List

def largestGoodInteger(num: str) -> str:
    max_val = "-1"
    i = 0
    while i < len(num)-2:
        if num[i] == num[i+1] == num[i+2]:
            max_val = max(max_val, num[i])
            i += 3
        else:
            i += 1
    
    return max_val * 3 if max_val != "-1" else ""

class largestGoodIntegerTest(unittest.TestCase):
    def test_largestGoodInteger_case1(self, num="6777133339", solution="777"):
        output = largestGoodInteger(num)
        self.assertEqual(output, solution)

    def test_largestGoodInteger_case2(self, num="2300019", solution="000"):
        output = largestGoodInteger(num)
        self.assertEqual(output, solution)
        
    def test_largestGoodInteger_case3(self, num="42352338", solution=""):
        output = largestGoodInteger(num)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()