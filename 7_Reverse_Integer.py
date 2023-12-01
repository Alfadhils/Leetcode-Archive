import unittest

def reverse(x: int) -> int:
    neg = -1 if x<0 else 1
    res = int(str(abs(x))[::-1])*neg
    false = -(2**31) <= res <= 2**31 - 1

    return res if false else 0

class reverseTest(unittest.TestCase):
    def test_reverse_case1(self, x=123, solution=321):
        output = reverse(x)
        self.assertEqual(output, solution)

    def test_reverse_case2(self, x=-123, solution=-321):
        output = reverse(x)
        self.assertEqual(output, solution)

    def test_reverse_case3(self, x=120, solution=21):
        output = reverse(x)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()