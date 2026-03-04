from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        rowCount = [0] * m
        colCount = [0] * n

        # pass 1: count 1s in rows and cols
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1

        # pass 2: count special positions
        ans = 0
        for i in range(m):
            if rowCount[i] == 0:   # small skip
                continue
            for j in range(n):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    ans += 1

        return ans