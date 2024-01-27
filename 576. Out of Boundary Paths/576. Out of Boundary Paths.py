class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def dp(x, y, moves, memo):
            if moves == 0:
                return 0

            if (x, y, moves) in memo:
                return memo[(x, y, moves)]

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            total_paths = 0

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    total_paths = (total_paths + dp(nx, ny, moves - 1, memo)) % (10**9 + 7)
                else:
                    total_paths += 1

            memo[(x, y, moves)] = total_paths
            return total_paths

        return dp(startRow, startColumn, maxMove, {})