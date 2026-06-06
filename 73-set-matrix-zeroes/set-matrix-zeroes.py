class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        #define len of rows
        m = len(matrix)
        #define len of columns
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    # mark entire row
                    # for col in range(n):
                    #     if matrix[i][col] != 0:
                    #         matrix[i][col] = -1
                    # # mark entire col
                    # for row in range(m):
                    #     if matrix[row][j] != 0:
                    #         matrix[row][j] = -1
        #replace -1 with 0
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0