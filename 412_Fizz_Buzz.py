import unittest
from typing import List

def fizzBuzz(n: int) -> List[str]:
    res = []
    for i in range(1,n+1):
        if i%15 == 0:
            res.append('FizzBuzz')
        elif i%5 == 0:
            res.append('Buzz')
        elif i%3 == 0:
            res.append('Fizz')
        else :
            res.append(str(i))

    return res

class fizzBuzzTest(unittest.TestCase):
    def test_fizzBuzz_case1(self, n=3, solution=["1","2","Fizz"]):
        output = fizzBuzz(n)
        self.assertEqual(output, solution)

    def test_fizzBuzz_case2(self, n=5, solution=["1","2","Fizz","4","Buzz"]):
        output = fizzBuzz(n)
        self.assertEqual(output, solution)

    def test_fizzBuzz_case3(self, n=15, solution=["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]):
        output = fizzBuzz(n)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()