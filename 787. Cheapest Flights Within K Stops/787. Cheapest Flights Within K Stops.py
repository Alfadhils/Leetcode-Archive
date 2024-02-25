from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: {} for i in range(n)}
        for a, b, cost in flights:
            graph[a][b] = cost
        
        def dijkstra(graph, s, d, k):
            dist = {vertex: float('infinity') for vertex in graph}
            dist[s] = 0

            queue = [(0, s, k)]

            while queue:
                curr_dist, curr, count = queue.pop(0)

                for new, cost in graph[curr].items():
                    new_dist = curr_dist + cost
                    if new_dist < dist[new] and count > 0:
                        dist[new] = new_dist
                        queue.append((new_dist, new, count - 1))

            return dist[d]

        val = dijkstra(graph, src, dst, k + 1)
        return -1 if val == float('infinity') else val
