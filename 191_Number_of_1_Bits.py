import unittest

def hammingWeight(n: int) -> int:
    res = 0
    while n > 0:
        if n % 2 == 1:
            res += 1
        n = n//2
    return res

class hammingWeightTest(unittest.TestCase):
    def test_hammingWeight_case1(self, n=0b00000000000000000000000000001011, solution=3):
        output = hammingWeight(n)
        self.assertEqual(output, solution)

    def test_hammingWeight_case2(self, n=0b00000000000000000000000010000000, solution=1):
        output = hammingWeight(n)
        self.assertEqual(output, solution)

    def test_hammingWeight_case3(self, n=0b11111111111111111111111111111101, solution=31):
        output = hammingWeight(n)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()