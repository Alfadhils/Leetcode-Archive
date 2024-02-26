# 279. Perfect Squares

## Intuition

The intuition behind this problem is to find the minimum number of perfect square numbers that sum up to a given positive integer `n`.

## Approach

We can approach this problem using a breadth-first search (BFS) technique. We start from the given number `n` and keep subtracting perfect square numbers from it until we reach 0. At each step, we keep track of the number of perfect square numbers subtracted, which represents the number of steps needed to reach 0.

## Complexity

- Time complexity: O(n sqrt n)
  - Generating the list of perfect squares takes O(sqrt n) time.
  - The BFS process can take up to O(n) iterations.
- Space complexity: O(n)$
  - We use a set to keep track of visited numbers, which can take up to O(n) space.
  - The queue can also take up to O(n) space in the worst case.

## Code

```python
class Solution:
    def numSquares(self, n: int) -> int:
        visited = set()
        queue = deque([(n,0)])

        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
      
        while queue:
            num, step = queue.popleft()
            for square in squares:
                new = num - square
                if new == 0:
                    return step + 1
                elif new < 0:
                    break
                elif new not in visited:
                    visited.add(num - square)
                    queue.append((num - square, step + 1))

        return 1
```
