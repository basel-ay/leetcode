class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # empty validation
        if not matrix:
            return []

        m = len(matrix)  # rows
        n = len(matrix[0])  # columns

        zeros_row = [False] * m
        zeros_col = [False] * n
        
        # detect rows and columns to be changed
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeros_row[row] = True
                    zeros_col[col] = True
        
        # replace detected rows and columns with 0s
        for row in range(m):
            for col in range(n):
                if zeros_row[row] or zeros_col[col]:
                    matrix[row][col] = 0