# 999. Available Captures for Rook

## Intuition
The problem requires finding the number of pawns that can be captured by a rook on a given chessboard. A rook can capture pawns in its horizontal or vertical path until it encounters another piece or the edge of the board.

## Approach
1. Find the position of the rook on the chessboard.
2. Check the horizontal path to the right of the rook until a pawn ('p') or a bishop ('B') is encountered.
3. Check the horizontal path to the left of the rook until a pawn ('p') or a bishop ('B') is encountered.
4. Check the vertical path downwards from the rook until a pawn ('p') or a bishop ('B') is encountered.
5. Check the vertical path upwards from the rook until a pawn ('p') or a bishop ('B') is encountered.
6. Count the number of pawns encountered in all four directions.

## Complexity
- Time complexity: O(rows * cols), where rows and cols are the dimensions of the chessboard. In the worst case, we iterate through all cells of the board.
- Space complexity: O(1), as we use a constant amount of extra space.

## Code
```python
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
