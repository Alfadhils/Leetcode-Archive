from typing import List
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