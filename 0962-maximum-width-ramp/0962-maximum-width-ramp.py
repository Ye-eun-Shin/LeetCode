class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # 1. Decreasing stack to store the indices of decreasing elements
        stack = []
        
        # Create a stack of indices where nums[stack[i]] is in decreasing order
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        max_ramp = 0
        # 2. Traverse from the end to find the largest ramp
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                max_ramp = max(max_ramp, i - stack.pop())
        
        return max_ramp