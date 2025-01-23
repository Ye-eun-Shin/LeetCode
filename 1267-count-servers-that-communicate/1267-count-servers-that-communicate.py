class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        servers = set()
        column = [[] for _ in range(n)] # (i,j) : i번째 column의 j번째 row
        # 효율 약간 똥망
        # servers에 후보지를 넣고.. 중복은 없도록 set 활용
        # 첫번째 row first 탐색에서 column 방향 탐색 할 필요 없도록 미리 탐색을 해놓는다..!
        
        for i in range(m):
            cnt = grid[i].count(1)
            if cnt == 0:
                continue
            elif cnt == 1:
                idx = grid[i].index(1)
                column[idx].append(i)
                continue
            for j in range(n):
                if grid[i][j]:
                    servers.add((i, j))
                    column[j].append(i)
        
        for j in range(n):
            cnt = len(column[j])
            if cnt <= 1:
                continue
            for i in column[j]:
                servers.add((i,j))
        
        return len(servers)
