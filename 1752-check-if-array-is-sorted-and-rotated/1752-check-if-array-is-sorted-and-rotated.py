class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            nums[i] = (nums[i], i)
        
        nums = sorted(nums)
        prior = nums[0][1]
        first = False
        check = True
        for i in range(1, length):
            if nums[i][1]==0:
                if first:
                    check = False
                    break
                first = True
                prior = 0
            else:
                if nums[i][1]==prior+1:
                    prior+=1
                elif nums[i][0]!=nums[i-1][0]:
                    check = False
                    break
        return check
                