# 752. Open the Lock

## Intuition
The problem seems like a variation of a graph traversal problem, where each combination of the lock represents a node, and there are edges between nodes representing the possible rotations of each wheel.

## Approach
We can use breadth-first search (BFS) to traverse through all possible combinations of the lock, starting from the initial combination '0000'. At each step, we generate all possible combinations that can be reached from the current combination by rotating one of the wheels either clockwise or counterclockwise. We continue this process until we find the target combination or exhaust all possible combinations.

## Complexity
- Time complexity:
  The worst-case time complexity is O(10^4 * d), where d is the number of wheels (here, 4). Since each wheel has 10 possible states (0-9), and there are d wheels, the total number of combinations is 10^d. We need to traverse through all possible combinations, and for each combination, we need to generate its neighbors, which takes O(d) time.
  O(10^4 * 4) = O(40,000)

- Space complexity:
  The space complexity is dominated by the space required for the sets 'deadends', 'visited', and 'queue'. In the worst case, all combinations can be in either 'deadends' or 'visited', so both can take up to O(10^4) space. The queue can also take O(10^4) space in the worst case. Hence, the overall space complexity is O(10^4).
  O(10^4)

## Code
```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0

        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        visited = set()
        queue = {'0000'}

        steps = 0

        while queue:
            next_queue = set()
            steps += 1

            for node in queue:
                for i in range(4):
                    for diff in [-1, 1]:
                        new_digit = (int(node[i]) + diff) % 10
                        new_node = node[:i] + str(new_digit) + node[i+1:]

                        if new_node in deadends or new_node in visited:
                            continue

                        if new_node == target:
                            return steps

                        visited.add(new_node)
                        next_queue.add(new_node)

            queue = next_queue

        return -1
