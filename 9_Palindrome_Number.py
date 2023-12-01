import unittest

def isPalindrome(x: int) -> bool:
    x_str = str(x)
    return x_str == x_str[::-1]

class isPalindromeTest(unittest.TestCase):
    def test_isPalindrome_case1(self, x=121, solution=True):
        output = isPalindrome(x)
        self.assertEqual(output, solution)

    def test_isPalindrome_case2(self, x=-121, solution=False):
        output = isPalindrome(x)
        self.assertEqual(output, solution)

    def test_isPalindrome_case3(self, x=10, solution=False):
        output = isPalindrome(x)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()