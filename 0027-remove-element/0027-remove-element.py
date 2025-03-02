class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i=0 # 수정할 인덱스
        for j in range(length):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i