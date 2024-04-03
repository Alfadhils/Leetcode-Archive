# 79. Word Search
## Intuition
The problem is asking to determine if a word exists in a 2D board of letters. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Approach
We can solve this problem using a depth-first search (DFS) approach. We iterate through each cell of the board, and for each cell, we start a DFS search to check if the word can be formed starting from that cell. We continue the DFS search until we find the word or exhaust all possible paths. We use backtracking to explore all possible directions.

## Complexity
- Time complexity: O(N * M * 4^L), where N is the number of rows in the board, M is the number of columns in the board, and L is the length of the word. We explore all possible combinations from each cell in the board.
- Space complexity: O(L), where L is the length of the word. The space is primarily used for the recursion stack.

## Code
```python
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
```
