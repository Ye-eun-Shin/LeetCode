class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n
        
        # backtracking... 각 index에서의 선택지
        # 지금까지의 결과에
        # idx +1 ~끝까지 하나씩만 or 더 해본다.
        # max_or과 동일하다면 subset number+1

        cnt = 0

        # idx: 현재까지 탐색한 index, subset : 현재까지 수집한 subset
        def backtracking(idx, subset, or_res):
            nonlocal cnt
            for i in range(idx+1, len(nums)):
                tmp = or_res|nums[i]
                if tmp==max_or:
                    cnt+=1
                backtracking(i, subset+[nums[i]], tmp)
        
        backtracking(-1, [], 0)
        return cnt
