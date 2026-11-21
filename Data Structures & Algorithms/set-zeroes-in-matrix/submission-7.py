class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # matrix=matrix
        zer = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        zer=True

        R = len(matrix)
        C = len(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if matrix[0][0] ==0:
            for c in range(R):
                matrix[c][0] = 0

        if zer:
            matrix[0] = [0]*C

                




        # return matrix