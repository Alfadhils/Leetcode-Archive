class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counts = [0] * (n + 1)
        trusting = set()

        for a, b in trust:
            trust_counts[b] += 1
            trusting.add(a)

        for i in range(1, n + 1):
            if trust_counts[i] == n - 1 and i not in trusting:
                return i

        return -1