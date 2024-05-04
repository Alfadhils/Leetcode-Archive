# 881. Boats to Save People
## Intuition
The intuition behind this problem is to maximize the number of people rescued using as few boats as possible. Since each boat has a weight limit, we want to pair the heaviest person with the lightest person that can fit in the boat, and then iterate through the sorted list of people to determine the number of boats needed.

## Approach
The approach involves sorting the list of people in descending order of weight, then using two pointers to traverse the list from both ends. At each step, we check if the combined weight of the heaviest and lightest person within the current window is less than or equal to the boat's weight limit. If it is, we increment the right pointer (representing the heaviest person) and decrement the left pointer (representing the lightest person). If not, we only increment the left pointer. We continue this process until the left pointer surpasses the right pointer, indicating we've considered all people. The number of boats needed is then determined by the position of the left pointer.

## Complexity
- Time complexity: 
  - Sorting the list takes O(n log n) time, where n is the number of people. 
  - Traversing the list takes O(n) time.
  - Therefore, the overall time complexity is O(n log n).
  
- Space complexity:
  - The only additional space used is for the pointers, which takes constant space.
  - Hence, the space complexity is O(1).

## Code
``` python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1

        return left
```