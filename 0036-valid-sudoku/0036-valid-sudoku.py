class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # r번째 row가 과연 valid한가
        def isValidRow(r: int):
            check = [0 for _ in range(10)]
            target = board[r]
            for i in range(9):
                if target[i]=='.':
                    continue
                # 이미 나왔던 값이면
                if check[int(target[i])]:
                    return False
                check[int(target[i])]=1
            
            return True
        
        # c번째 column이 과연 valid한가
        def isValidCol(c: int):
            check = [0 for _ in range(10)]
            for i in range(9):
                if board[i][c]=='.':
                    continue
                # 이미 나왔던 값이면
                if check[int(board[i][c])]:
                    return False
                check[int(board[i][c])]=1
            
            return True

        # (i,j)번째 sub-box가 과연 valid한가
        def isValidBox(i, j):
            check = [0 for _ in range(10)]
            for m in range(3*i, 3*(i+1)):
                for n in range(3*j, 3*(j+1)):
                    if board[m][n]=='.':
                        continue
                    if check[int(board[m][n])]:
                        return False
                    check[int(board[m][n])]=1
            
            return True

        for i in range(9):
            if not isValidRow(i) or not isValidCol(i):
                return False
            
            r = i//3
            c = i%3
            if not isValidBox(r, c):
                return False
    
        
        return True