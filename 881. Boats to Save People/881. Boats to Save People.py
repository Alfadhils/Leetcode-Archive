from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1

        return left