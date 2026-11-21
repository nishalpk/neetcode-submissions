class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def islands(i,j):
            if  i<0 or j<0 or i>=m or j>=n or grid[i][j]=="0":
                return
            grid[i][j]="0"
            islands(i+1,j)
            islands(i,j+1)
            islands(i-1,j)
            islands(i,j-1)
            return 1
            
            

            
        c= 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands(i,j)
                    c+=1

        return c
        

        