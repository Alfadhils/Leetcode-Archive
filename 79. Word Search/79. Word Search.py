from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])
        
        def solve(x, y, target, seen):
            if len(target) == 0:
                return True
            
            if x < 0 or x >= h or y < 0 or y >= w or board[x][y] != target[0] or (x, y) in seen:
                return False

            seen.add((x, y))
            result = solve(x - 1, y, target[1:], seen) or \
                     solve(x + 1, y, target[1:], seen) or \
                     solve(x, y - 1, target[1:], seen) or \
                     solve(x, y + 1, target[1:], seen)
            seen.remove((x, y))
            return result

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if solve(i, j, word, set()):
                        return True
        return False