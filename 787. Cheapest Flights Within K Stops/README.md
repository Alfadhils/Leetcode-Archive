# 787. Cheapest Flights Within K Stops

## Intuition

The problem seems like a graph traversal problem where we need to find the cheapest flight within a certain number of stops. One common approach for such problems is to use Dijkstra's algorithm with a slight modification to keep track of the number of stops as well.

## Approach

We can model the flights as a graph where each node represents an airport, and each edge represents a flight between two airports with an associated cost. We then apply Dijkstra's algorithm to find the shortest path from the source airport to the destination airport with the constraint on the number of stops allowed.

We will modify Dijkstra's algorithm to keep track of the number of stops made so far. We'll continue exploring paths until we reach the destination or exceed the maximum number of stops allowed.

## Complexity

- Time complexity:
  - Building the graph: O(E), where E is the number of edges (flights)
  - Dijkstra's algorithm: O((V + E) * log(V)), where V is the number of vertices (airports) and E is the number of edges (flights)
    Overall time complexity: O((V + E) * log(V))
- Space complexity:
  - Storing the graph: O(V + E)
  - Storing distances and other data: O(V)
    Overall space complexity: O(V + E)

## Code

```python
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
```
