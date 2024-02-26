from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = sum(accounts[0])
        for i in accounts:
            if sum(i)> maxwealth:
                maxwealth = sum(i)
        return maxwealth