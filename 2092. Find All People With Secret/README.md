# 2092. Find All People With Secret

## Intuition
The problem involves finding all people who have the secret knowledge within a network of meetings. The approach here seems to utilize graph traversal techniques to identify individuals who gain the secret knowledge over time.

## Approach
The solution maintains a set called `know` to keep track of individuals who possess the secret knowledge. It iterates through the meetings sorted by time and constructs a graph representation of the relationships between individuals who attend meetings together. It then performs a breadth-first search (BFS) starting from the individuals who already have the secret knowledge, marking new individuals as knowledgeable and adding them to the BFS queue.

## Complexity
- Time complexity: The time complexity depends on the number of meetings and the size of the meeting attendees. In the worst case, it can be approximated as O(n^2), where n is the number of meetings.
- Space complexity: The space complexity is dominated by the size of the `know` set and the graph representation. It can be approximated as O(n), where n is the number of individuals in the network.

## Code
```python
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
