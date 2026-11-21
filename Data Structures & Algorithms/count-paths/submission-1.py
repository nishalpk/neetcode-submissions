class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mp = [[-1]*n for i in range(m) ]

        # for i in range(m):
        #     for j in range(n):

        def paths(i,j) ->int:
            if i==(m-1) and j==(n-1):
                return 1
            if i>m-1 or j>n-1:
                return 0
            

            if mp[i][j] != -1:
                return mp[i][j]
            mp[i][j] = paths(i+1,j)+paths(i,j+1)
            return mp[i][j]
        
        return paths(0,0)