import unittest
from typing import List

def findMatrix(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    j = 0
    for i in range(len(nums)):
        if i<1:
            res.append([nums[i]])
            continue

        if nums[i] == nums[i-1]:
            res[j].append(nums[i])
        else :
            res.append([nums[i]])
            j += 1
        
    output_list = []

    max_length = max(len(sublist) for sublist in res)
    for i in range(max_length):
        new_sublist = []
        for sublist in res:
            if i < len(sublist):
                new_sublist.append(sublist[i])
        output_list.append(new_sublist)
    
    return output_list

class findMatrixTest(unittest.TestCase):
    def test_findMatrix_case1(self, nums=[1,3,4,1,2,3,1], solution=[[1,2,3,4],[1,3],[1]]):
        output = findMatrix(nums)
        self.assertEqual(output, solution)

    def test_findMatrix_case2(self, nums=[2,1,1], solution=[[1,2],[1]]):
        output = findMatrix(nums)
        self.assertEqual(output, solution)
        
    def test_findMatrix_case3(self, nums=[1,2,3,3,2,1], solution=[[1,2,3],[1,2,3]]):
        output = findMatrix(nums)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()