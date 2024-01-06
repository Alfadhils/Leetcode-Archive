import unittest

def numberOfWays(corridor: str) -> int:
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

class numberOfWaysTest(unittest.TestCase):
    def test_numberOfWays_case1(self, corridor="SSPPSPS", solution=3):
        output = numberOfWays(corridor)
        self.assertEqual(output, solution)

    def test_numberOfWays_case2(self, corridor="S", solution=0):
        output = numberOfWays(corridor)
        self.assertEqual(output, solution)

    def test_numberOfWays_case3(self, corridor="PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS", solution=919999993):
        output = numberOfWays(corridor)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()
