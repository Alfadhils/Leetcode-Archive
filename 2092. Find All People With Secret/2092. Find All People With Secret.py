from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know = set([0, firstPerson])

        meetings.sort(key=lambda x: x[2])
        size = len(meetings)
        i = 0
        while i < size:
            curr_time = meetings[i][2]
            graph = defaultdict(list)
            curr_know = set()
            while i < size and meetings[i][2] == curr_time:
                graph[meetings[i][0]].append(meetings[i][1])
                graph[meetings[i][1]].append(meetings[i][0])

                if meetings[i][0] in know:
                    curr_know.add(meetings[i][0])
                if meetings[i][1] in know:
                    curr_know.add(meetings[i][1])

                i += 1
            
            queue = deque(curr_know)

            while queue:
                for _ in range(len(queue)):
                    person = queue.popleft()
                    for neighbor in graph[person]:
                        if neighbor not in know:
                            know.add(neighbor)
                            queue.append(neighbor)
                        
        return list(know)