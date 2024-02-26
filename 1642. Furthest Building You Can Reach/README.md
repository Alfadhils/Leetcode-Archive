# 1642. Furthest Building You Can Reach
## Intuition
The problem asks us to find the furthest building we can reach with either bricks or ladders given certain constraints. To approach this, we need to iterate through the buildings and keep track of the differences in heights between adjacent buildings. Whenever the height difference is positive (meaning we need to use bricks or ladders to climb), we prioritize using ladders if possible and fallback to bricks if not enough ladders are available.

## Approach
We iterate through the buildings, calculating the difference in heights between adjacent buildings. If the difference is positive (meaning we need to climb), we add it to a min-heap. We prioritize using ladders by checking if we have enough ladders available. If we don't, we use bricks instead. We keep track of the total bricks used and return the index of the last building we could reach.

## Complexity
- Time complexity: O(n log k), where n is the number of buildings and k is the number of ladders available.
  - The time complexity is dominated by the operations of adding and removing elements from the heap, which takes O(log k) time for each building.
- Space complexity: O(k)
  - We use a min-heap to store at most k elements (height differences), so the space complexity is O(k).

## Code
```python
import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pq = [] 
        
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(pq, diff)
                if len(pq) > ladders:
                    bricks -= heapq.heappop(pq)
                if bricks < 0:
                    return i
        
        return n - 1
```