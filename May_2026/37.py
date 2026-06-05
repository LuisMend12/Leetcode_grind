# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
from collections import defaultdict

from narwhals import List


from ast import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = int(board[i][j])
                    r[i].add(num)
                    c[j].add(num)
                    b[(i // 3, j // 3)].add(num)

        def backtrack(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            for num in range(1, 10):
                if num not in r[i] and num not in c[j] and num not in b[(i // 3, j // 3)]:
                    board[i][j] = str(num)
                    r[i].add(num)
                    c[j].add(num)
                    b[(i // 3, j // 3)].add(num)

                    if backtrack(index + 1):
                        return True

                    board[i][j] = '.'
                    r[i].remove(num)
                    c[j].remove(num)
                    b[(i // 3, j // 3)].remove(num)

            return False    
        backtrack(0)
        return board
