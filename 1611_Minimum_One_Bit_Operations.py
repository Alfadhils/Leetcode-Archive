import unittest

def minimumOneBitOperations(n: int) -> int:
    binary = bin(n)[2:]
    length = len(binary)
    res = 0
    state = 0

    for i, bit in enumerate(binary):
        if bit == '1':
            state ^= 1

        res += (1 << (length - 1 - i)) * state

    return res

class minimumOneBitOperationsTest(unittest.TestCase):
    def test_minimumOneBitOperations_case1(self, n=3, solution=2):
        output = minimumOneBitOperations(n)
        self.assertEqual(output, solution)

    def test_minimumOneBitOperations_case2(self, n=6, solution=4):
        output = minimumOneBitOperations(n)
        self.assertEqual(output, solution)

    def test_minimumOneBitOperations_case3(self, n=8, solution=15):
        output = minimumOneBitOperations(n)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()