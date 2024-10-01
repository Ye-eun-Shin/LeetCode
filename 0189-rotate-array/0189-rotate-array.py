class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k가 length보다 길 수도 있다. => 나머지를 k로 생각.
        lens = len(nums)
        k %= lens
        nums[:] = nums[lens-k:]+nums[:lens-k]
