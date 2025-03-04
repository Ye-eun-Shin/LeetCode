class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 피보나치 감성 아닐까..?
        answer = [[] for _ in range(numRows)]
        answer[0].append(1)
        for i in range(1, numRows):
            answer[i].append(1)
            for j in range(1, i):
                answer[i].append(answer[i-1][j-1]+answer[i-1][j])
            answer[i].append(1)
        
        return answer
