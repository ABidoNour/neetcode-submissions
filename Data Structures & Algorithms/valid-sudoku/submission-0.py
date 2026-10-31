class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(9):
            row_set = set()
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue
                square_r,square_c = i // 3 , j // 3
                square_i = (square_r * 3) + square_c
                if curr in row_set or curr in cols[j] or curr in squares[square_i]:
                    return False
                row_set.add(curr)
                cols[j].add(curr)
                squares[square_i].add(curr)
        return True