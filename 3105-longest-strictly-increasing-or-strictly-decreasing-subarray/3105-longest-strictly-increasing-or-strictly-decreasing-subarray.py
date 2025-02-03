class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # gradient를.. 생각 : 1 / 0 / -1 
        # ex) [1,4,3,3,2] => [1,-1,0,-1]
        # ex) [3,3,3,3] => [0,0,0]
        # ex) [3,2,1] => [-1,-1]
        gradients = []
        length = len(nums)
        for i in range(1, length):
            if nums[i]>nums[i-1]:
                gradients.append(1)
            elif nums[i]==nums[i-1]:
                gradients.append(0)
            else:
                gradients.append(-1)

        gradients.append(2) # 마지막 temp->longest 업데이트를 위함
        longest = 1
        if gradients[0]:
            temp=2
        else:
            temp=1
        for i in range(1, length):
            if gradients[i] and gradients[i]==gradients[i-1]:
                temp+=1
            else:
                longest = max(temp, longest)
                if gradients[i]:
                    temp=2
                else:
                    temp=1

        return longest