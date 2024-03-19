# 621. Task Scheduler
## Intuition
The problem requires us to schedule tasks in such a way that there is a cooldown period n between identical tasks. We need to find the minimum time needed to execute all tasks.

## Approach
We can use a greedy approach to solve this problem. We can keep track of the frequency of each task using a Counter. Then, we iterate through the tasks and schedule them in such a way that the most frequent tasks are executed first. We use a priority queue `maxheap` to keep track of the tasks based on their frequencies. We also use a deque to keep track of the tasks that are waiting due to the cooldown period.

## Complexity
- Time complexity:
  - Building the Counter: O(n)
  - Building the maxheap: O(n log m), where m is the number of unique tasks
  - Iterating through tasks: O(n)
  - Overall time complexity: O(n log m)

- Space complexity:
  - Count dictionary: O(m), where m is the number of unique tasks
  - Maxheap: O(m)
  - Queue: O(n)
  - Overall space complexity: O(m + n)

## Code
```python
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0
        queue = deque()
        maxheap = []
        
        for freq in count.values():
            heapq.heappush(maxheap, -freq) 

        while maxheap or queue:
            time += 1
            if maxheap:
                cnt = heapq.heappop(maxheap)
                update_cnt = cnt + 1
                if update_cnt:
                    queue.append([update_cnt, time + n])
            
            if queue and time == queue[0][1]:
                heapq.heappush(maxheap, queue.popleft()[0])

        return time
```