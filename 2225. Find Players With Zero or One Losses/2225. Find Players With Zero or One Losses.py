from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        res1 = []
        res2 = []
        for match in matches:
            if match[0] not in win:
                win[match[0]] = 0

            if match[1] in win:
                win[match[1]] += 1
            else :
                win[match[1]] = 1
        
        for key in win:
            if win[key] == 0:
                res1.append(key)
            elif win[key] == 1:
                res2.append(key)

        return [sorted(res1),sorted(res2)]
        