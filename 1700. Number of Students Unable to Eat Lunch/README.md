# 1700. Number of Students Unable to Eat Lunch
## Intuition
The problem involves simulating the process of students taking sandwiches. We need to find the number of students who will be unable to eat lunch, given the order in which they can take their sandwiches.

## Approach
The approach is to simulate the process of students taking sandwiches until either all students have taken their sandwiches or no more changes can occur. We use two dequeues to represent the students and sandwiches. We iterate through the students and sandwiches simultaneously, checking if the current student can take the sandwich. If a student cannot take the sandwich, we move them to the end of the queue. If we loop through all students without any changes happening, we break the loop to avoid infinite iteration. If all students are unable to take their sandwiches, we return the count of remaining students.

## Complexity
- Time complexity:
  - The time complexity of this solution is O(n), where n is the number of students. In the worst case, each student may need to be checked twice.
- Space complexity:
  - The space complexity is also O(n) because we are using two deques to store the students and sandwiches.

## Code
```python
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
```