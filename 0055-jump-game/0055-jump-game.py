class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1  # 도달해야 하는 마지막 위치
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i  # 도달 가능한 위치 갱신
        
        return last_pos == 0