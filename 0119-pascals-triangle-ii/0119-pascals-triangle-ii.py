class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pt = [[1 for _ in range(rowIndex+1)] for _ in range(2)]
        for i in range(1, rowIndex+1):
            pidx = i%2
            for j in range(1, i):
                prior = int(not pidx)
                pt[pidx][j]=pt[prior][j-1]+pt[prior][j]
            pt[pidx][i]=1
        
        return pt[rowIndex%2][:rowIndex+1]
