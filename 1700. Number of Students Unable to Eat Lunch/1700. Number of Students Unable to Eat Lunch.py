from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        dqst, dqsa = deque(students), deque(sandwiches)
        count = 0
        while dqst and dqsa :
            if count == n:
                return n

            curr = dqst.popleft()
            if curr == dqsa[0]:
                n -= 1
                count = 0
                dqsa.popleft()
            else :
                count += 1
                dqst.append(curr)

        return 0
        