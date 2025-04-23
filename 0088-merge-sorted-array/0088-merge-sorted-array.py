class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        temp = []
        while True:
            if i>=m and j>=n:
                break
            if i>=m:
                temp.append(nums2[j])
                j+=1
            elif j>=n:
                temp.append(nums1[i])
                i+=1
            elif nums1[i]<=nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        for i in range(m+n):
            nums1[i] = temp[i]