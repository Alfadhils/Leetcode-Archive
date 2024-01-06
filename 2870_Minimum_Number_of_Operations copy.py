import unittest
from typing import List

def minOperations(nums: List[int]) -> int:
    n_dict = {}
    for n in nums:
        if n in n_dict:
            n_dict[n] += 1
        else :
            n_dict[n] = 1
    
    count = 0 
    for val in n_dict.values():
        if val == 1 :
            return -1
        count += (val-1)//3 + 1
    
    return count

class minOperationsTest(unittest.TestCase):
    def test_minOperations_case1(self, nums=[2,3,3,2,2,4,2,3,4], solution=4):
        output = minOperations(nums)
        self.assertEqual(output, solution)

    def test_minOperations_case2(self, nums=[2,1,2,2,3,3], solution=-1):
        output = minOperations(nums)
        self.assertEqual(output, solution)
        
    def test_minOperations_case3(self, nums=[1,3,1,2,1,3,1,2,1], solution=4):
        output = minOperations(nums)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()