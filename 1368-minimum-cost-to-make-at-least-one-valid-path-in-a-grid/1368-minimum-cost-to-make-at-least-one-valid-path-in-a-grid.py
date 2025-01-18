import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # bfs 해서 거기까지 도달하는 데 최소 몇번을 수정해야 할지..
        # 다만 이제.. heap을 곁들인..
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        size_x = len(grid)
        size_y = len(grid[0])
        def in_range(x,y):
            if 0<=x<size_x and 0<=y<size_y:
                return True
            return False
        
        q = []
        visited = [[0 for _ in range(size_y)] for _ in range(size_x)]
        cost = [[size_x*size_y for _ in range(size_y)] for _ in range(size_x)]
        heapq.heappush(q, (0, (0,0))) # 우선순위는 지금까지의 최소 cost, 그 다음이 좌표
        cost[0][0]=0
        answer = 0
        while q:
            _, xy = heapq.heappop(q)
            x, y = xy
            visited[x][y]=1
            pcost = cost[x][y]
            if x==size_x-1 and y==size_y-1:
                answer = pcost
                break
            for i in range(4):
                xx = x+dx[i]
                yy = y+dy[i]

                if not in_range(xx, yy):
                    continue
                
                if i+1==grid[x][y]:
                    ncost = pcost
                else:
                    ncost = pcost+1
                
                if ncost<cost[xx][yy]:
                    cost[xx][yy]=ncost
                    if not visited[xx][yy]:
                        heapq.heappush(q, (ncost, (xx,yy)))

        return answer