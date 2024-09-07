class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums 중 두 요소를 합쳐 target 값이 나올 때 두 요소의 index 리스트 반환
        # brute force(완탐) 사용 
        
        num_len = len(nums)
        for i in range(num_len-1):
            for j in range(i+1, num_len):
                if nums[i]+nums[j]==target:
                    return [i,j]