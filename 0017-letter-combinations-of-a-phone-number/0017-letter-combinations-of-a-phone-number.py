class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dg_map = {'2':'abc', '3' : 'def', '4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        """
        1. 백트래킹 : 더이상 입력된 digit이 존재하지 않는다면 재귀 반복을 종료한다.
        2. 재귀 : 어떠한 digit이 입력되었을 때, 발생할 수 있는 모든 경우를 지금까지의 모든 경우와 조합한다.
        """

        def recursion(d: str, comb: list):
            target = dg_map[d]
            new_res = []
            if len(comb)==0:
                for new in target:
                    new_res.append(new)
                return new_res
            
            for new in target:
                for old in comb:
                    new_res.append(old+new)
            
            return new_res

        output = []
        for d in digits:
            output = recursion(d, output)
        
        return output