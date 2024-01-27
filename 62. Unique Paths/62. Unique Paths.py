class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(x, y, memo):
            key = tuple(sorted((x, y)))

            if key in memo:
                return memo[key]

            if x == 1 or y == 1:
                return 1

            memo[key] = dp(x - 1, y, memo) + dp(x, y - 1, memo)
            return memo[key]

        return dp(m, n, {})
        