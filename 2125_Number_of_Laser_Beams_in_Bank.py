import unittest
from typing import List

def numberOfBeams(bank: List[str]) -> int:
        if len(bank)<2:
            return 0

        total=0
        i=0
        while True:
            c = bank[i].count('1')
            while '1' not in bank[i+1]:
                if i+1 == len(bank)-1 :
                    break
                i+=1
            n = bank[i+1].count('1')
            total += c*n
            if i+1 == len(bank)-1 :
                break
            i+=1
        
        return total

class numberOfBeamsTest(unittest.TestCase):
    def test_numberOfBeams_case1(self, bank=["011001","000000","010100","001000"], solution=8):
        output = numberOfBeams(bank)
        self.assertEqual(output, solution)

    def test_numberOfBeams_case2(self, bank=["000","111","000"], solution=0):
        output = numberOfBeams(bank)
        self.assertEqual(output, solution)
        
    def test_numberOfBeams_case3(self, bank=["00001","00010","00100","11111","00001","00010","00100"], solution=14):
        output = numberOfBeams(bank)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()