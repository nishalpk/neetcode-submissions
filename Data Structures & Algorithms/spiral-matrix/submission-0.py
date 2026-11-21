class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        M = len(matrix)
        N = len(matrix[0])
        l,r,t,b = 0,N-1,0,M-1
        w = [(0,1),(1,0),(0,-1),(-1,0)]
        steps = [len(matrix[0]),len(matrix)]
        d=0
        r,c = 0,-1
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += w[d][0]
                c += w[d][1]
                res.append(matrix[r][c])
            d+=1
            d%=4
            steps[d&1]-=1

        return res