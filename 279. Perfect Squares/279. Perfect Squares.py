from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        visited = set()
        queue = deque([(n,0)])

        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        
        while queue:
            num, step = queue.popleft()
            for square in squares:
                new = num-square
                if new == 0:
                    return step + 1
                elif new < 0:
                    break
                elif new not in visited:
                    visited.add(num - square)
                    queue.append((num - square, step + 1))

        return 1