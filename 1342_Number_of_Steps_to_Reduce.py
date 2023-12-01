import unittest

def numberOfSteps(num: int) -> int:
    count = 0
    while num > 0 :
        if num%2 : 
            num -= 1
        else :
            num /= 2
        
        count += 1

    return count

class numberOfStepsTest(unittest.TestCase):
    def test_numberOfSteps_case1(self, num=14, solution=6):
        output = numberOfSteps(num)
        self.assertEqual(output, solution)

    def test_numberOfSteps_case2(self, num=8, solution=4):
        output = numberOfSteps(num)
        self.assertEqual(output, solution)

    def test_numberOfSteps_case3(self, num=123, solution=12):
        output = numberOfSteps(num)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()