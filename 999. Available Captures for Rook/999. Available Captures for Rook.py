from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        total = 0
        rows, cols = len(board), len(board[0])

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'R':
                    rook_x, rook_y = x, y
                    break

        for y in range(rook_y + 1, cols):
            if board[rook_x][y] == 'p':
                total += 1
                break
            elif board[rook_x][y] == 'B':
                break

        for y in range(rook_y - 1, -1, -1):
            if board[rook_x][y] == 'p':
                total += 1
                break
            elif board[rook_x][y] == 'B':
                break

        for x in range(rook_x + 1, rows):
            if board[x][rook_y] == 'p':
                total += 1
                break
            elif board[x][rook_y] == 'B':
                break

        for x in range(rook_x - 1, -1, -1):
            if board[x][rook_y] == 'p':
                total += 1
                break
            elif board[x][rook_y] == 'B':
                break

        return total
