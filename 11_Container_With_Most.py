import unittest
from typing import List

def maxArea(height: List[int]) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        w = right - left

        if h*w > max_area :
            max_area = h*w

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

class maxAreaTest(unittest.TestCase):
    def test_maxArea_case1(self, height=[1,8,6,2,5,4,8,3,7], solution=49):
        output = maxArea(height)
        self.assertEqual(output, solution)

    def test_maxArea_case2(self, height=[1,1], solution=1):
        output = maxArea(height)
        self.assertEqual(output, solution)

    def test_maxArea_case3(self, height=[1,2,3,4,5,6,7,8,9], solution=20):
        output = maxArea(height)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()