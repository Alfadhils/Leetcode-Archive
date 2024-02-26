class Solution:
    def numberOfWays(self, corridor: str) -> int:
        scount, ways, total, res = 0, 0, 1, []

        for char in corridor:
            if char == 'S':
                if scount % 2:
                    res.append(ways)
                    ways = 0
                scount += 1
            elif char == 'P' and not scount % 2:
                ways += 1

        if scount % 2 or scount < 2:
            return 0

        for num in res[1:]:
            total = (total * (num + 1)) % (10**9 + 7)

        return total