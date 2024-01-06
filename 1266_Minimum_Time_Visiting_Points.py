import unittest
from typing import List

def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    prev = points[0]
    total = 0
    for point in points[1:]:
        time = max(abs(point[0]-prev[0]),abs(point[1]-prev[1]))
        total += time
        prev = point
    
    return total

class minTimeToVisitAllPointsTest(unittest.TestCase):
    def test_minTimeToVisitAllPoints_case1(self, points=[[1,1],[3,4],[-1,0]], solution=7):
        output = minTimeToVisitAllPoints(points)
        self.assertEqual(output, solution)

    def test_minTimeToVisitAllPoints_case2(self, points=[[3,2],[-2,2]], solution=5):
        output = minTimeToVisitAllPoints(points)
        self.assertEqual(output, solution)
    
    def test_minTimeToVisitAllPoints_case3(self, points=[[6,8],[8,6],[-4,4],[4,-4]], solution=22):
        output = minTimeToVisitAllPoints(points)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()