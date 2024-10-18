class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        def in_range(r, c):
            if 0<=r<m and 0<=c<n:
                return 1
            else:
                return 0

        def dfs(x, y):
            visited[x][y]=1
            for i in range(4):
                xx = x+dx[i]
                yy = y+dy[i]
                if not in_range(xx, yy):
                    continue
                if not visited[xx][yy] and grid[xx][yy]=='1':
                    dfs(xx, yy)

        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0':
                    continue
                elif visited[i][j]:
                    continue
                dfs(i,j)
                cnt+=1

        return cnt
        
