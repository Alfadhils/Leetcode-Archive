# 2385. Amount of Time for Binary Tree to Be Infected

## Intuition
The problem seems to involve traversing a binary tree to simulate the spread of infection, starting from a given node. We can utilize depth-first search (DFS) to construct a graph representation of the binary tree and then perform a breadth-first search (BFS) to track the infection spread.

## Approach
1. Construct a graph representation of the binary tree using DFS.
2. Perform BFS starting from the given start node to track the spread of infection.
3. Maintain a set to keep track of visited nodes to avoid revisiting nodes.
4. Increment the time each time a level of nodes is processed in BFS.

## Complexity
- Time complexity:
  - Building the graph: O(n), where n is the number of nodes in the binary tree.
  - BFS traversal: O(n), as we visit each node once.
  - Overall: O(n)
- Space complexity:
  - Graph representation: O(n)
  - Visited set: O(n)
  - Queue for BFS: O(n)
  - Overall: O(n)

## Code
```python
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time
```
