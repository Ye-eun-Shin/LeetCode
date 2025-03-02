class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # search? => binary search!!
        left = 0
        right = len(nums)-1
        answer = -1

        while True:
            if left>right:
                answer=right+1
                break
            mid = (left+right)//2
            if nums[mid]==target:
                answer=mid
                break
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return answer